#!/usr/bin/python3
"""
Script gathering the information about HTTP security headers usage based on the "MAJESTIC Top 1 million sites CSV file" data source.

No external dependency was used to faciliate the portability of the script.
"""
import urllib.request
import ssl
import sqlite3
import time
import concurrent.futures
from oshp_headers import OSHP_SECURITY_HEADERS

# Constants
NUMBER_OF_DOMAINS_TO_TAKE = 10000
VERBOSE = False
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
DATA_FOLDER = "../data"
THREADS_COUNT = 30
TIMEOUT = 10
DATA_DB_FILE = f"{DATA_FOLDER}/data.db"
CSV_INPUT_FILE = f"{DATA_FOLDER}/input.csv"

# Utility functions


def get_security_headers(url):
    sec_headers = {}
    try:
        # urllib follow redirect by default - Mimic browser requests
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        req = urllib.request.Request(url)
        req.add_header("User-Agent", USER_AGENT)
        req.add_header(
            "Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8")
        req.add_header("Accept-Language", "en-US,en;q=0.5")
        req.add_header("Accept-Encoding", "gzip, deflate, br")
        resp = urllib.request.urlopen(
            req, context=ctx, timeout=TIMEOUT)
        for header in resp.headers:
            if header.lower() in OSHP_SECURITY_HEADERS:
                sec_headers[header] = resp.headers[header]
    except Exception as e:
        # Used to identify that request did not succeed (ex: port closed or HTTP 4xx)
        if VERBOSE:
            print(f"\n[!] Error with url '{url}': {str(e)}.")
        sec_headers = None
    return sec_headers


def print_progress(msg):
    if VERBOSE:
        print(f"\r{msg}", end="", flush=True)


def worker(domain):
    try:
        # Start with HTTPS protocol to get security headers for the current domain
        print_progress(f"Analyse domain: {domain:80}")
        sec_headers = get_security_headers(f"https://{domain}")
        if sec_headers is None:
            # Fallback with HTTP protocol
            sec_headers = get_security_headers(f"http://{domain}")
        # Insert gathered headers for the current domain if present
        if sec_headers is not None and len(sec_headers) > 0:
            records = []
            for sec_header in sec_headers:
                records.append(
                    (domain, sec_header.lower(), sec_headers[sec_header]))
            with sqlite3.connect(DATA_DB_FILE, timeout=300) as connection:
                curs = connection.cursor()
                curs.executemany(
                    "INSERT INTO stats (domain,http_header_name,http_header_value) VALUES(?,?,?);", records)
        else:
            with sqlite3.connect(DATA_DB_FILE, timeout=300) as connection:
                curs = connection.cursor()
                curs.execute(
                    "INSERT INTO stats (domain,http_header_name,http_header_value) VALUES(?,NULL,NULL);", (domain,))

    except Exception as e:
        print(f"\n[!] Error with domain '{domain}': {str(e)}.")


if __name__ == "__main__":
    start_time = time.time()
    print("[+] Initialize DB...")
    with sqlite3.connect(DATA_DB_FILE) as connection:
        curs = connection.cursor()
        curs.execute(
            "CREATE TABLE IF NOT EXISTS stats (id integer PRIMARY KEY, domain text, http_header_name text, http_header_value text);")
        curs.execute("DELETE FROM stats;")
    print(
        f"[+] Start work using {THREADS_COUNT} workers in parallel taking first {NUMBER_OF_DOMAINS_TO_TAKE} domains...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS_COUNT) as executor:
        with open(CSV_INPUT_FILE, mode="r", encoding="utf-8") as f:
            lines = f.read().splitlines()[:NUMBER_OF_DOMAINS_TO_TAKE]
        for line in lines:
            executor.submit(worker, domain=line.split(",")[1].strip())
    print(f"\n[+] Data gathered: ")
    with sqlite3.connect(DATA_DB_FILE) as connection:
        curs = connection.cursor()
        curs.execute("SELECT max(id) from stats")
        for row in curs.fetchall():
            print(f"Records {row[0]}.")
    delay = round((time.time() - start_time) / 60)
    print(f"[+] Gathering performed in in {delay} minutes")
