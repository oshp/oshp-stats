# oshp-stats

[Statistics](stats.md) about HTTP response security headers usage mentioned by the OSHP.

See this [issue](https://github.com/OWASP/www-project-secure-headers/issues/61) for details.

# Data source

> MAJESTIC was used instead of the **CISCO Top 1 million sites CSV file** because it contain less malware domains.

* [MAJESTIC Top 1 million sites list](https://blog.majestic.com/development/majestic-million-csv-daily/).
* [CISCO Top 1 million sites CSV file](http://s3-us-west-1.amazonaws.com/umbrella-static/index.html).

```bash
# Download the MAJESTIC Top 1 million sites CSV file
$ wget http://downloads.majestic.com/majestic_million.csv
# Transform the downloaded file to an input source that use the same format 
# than the CISCO Top 1 million sites CSV file
$ cat majestic_million.csv | awk -F  "," 'NR>1 {print $1 "," $3}' > data/input.csv
$ rm majestic_million.csv
```

# Scripts

> They are all stored in the [scripts](scripts) folder and they are Python 3.x based.

The script [oshp_headers](scripts/oshp_headers.py) contains the HTTP headers suggested by the OSHP project. It is a configuration material.

* [gather_data](scripts/gather_data.py): Script gathering the information about HTTP security headers usage in a SQLITE database based on the "MAJESTIC Top 1 million sites CSV file" data source.
* [generate_stats_md_file](scripts/generate_stats_md_file.py): Script using the gathered data to generate/update the markdown file [stats](stats.md), with [mermaid pie charts](https://mermaid-js.github.io/mermaid/#/pie) with differents statistics about HTTP security headers usage.

# Data

> They are all stored in the [data](data) folder.

* [input.csv](data/input.csv): MAJESTIC Top 1 million sites list formated as one entry `number,domain` by line.
* [data.db](data/data.db): SQLITE database with information about HTTP security headers usage.
