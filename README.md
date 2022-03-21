# OWASP Secure Headers Project statistics

[Statistics](stats.md) about HTTP response security headers usage mentioned by the [OWASP Secure Headers Project](https://owasp.org/www-project-secure-headers/) (OSHP).

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

[Visual Studio Code](https://code.visualstudio.com/) is used for the scripts development. A Visual Studio Code [workspace file](project.code-workspace) is provided for the project.

Files:

* [gather_data](scripts/gather_data.py): Script gathering the information about HTTP security headers usage in a [SQLITE database](data/data.db) based on the "MAJESTIC Top 1 million sites CSV file" data source.
* [generate_stats_md_file](scripts/generate_stats_md_file.py): Script using the gathered data to generate/update the markdown file [stats](stats.md), with [mermaid pie charts](https://mermaid-js.github.io/mermaid/#/pie) with differents statistics about HTTP security headers usage.

# Data

> They are all stored in the [data](data) folder.

Files:

* [input.csv](data/input.csv): MAJESTIC Top 1 million sites list formated as one entry `ranking,domain` by line.
* [data.db](data/data.db): SQLITE database with information about HTTP security headers usage.

# Data and statistics update

> :information_source: Only the first 200000 entries of the CSV datasource are used to fit the processing timeframe allowed for a github action workfows using the free tiers.

The update is scheduled in the following way via [two dedicated github actions workfows](.github/workflows):

* The **first day** of every month the data database is updated.
* The **second day** of every month the statistic file is updated:
  * The files [input.csv](data/input.csv), [data.db](data/data.db) and [stats.md](stats.md) are attached to the build as artefacts. Therefore, it is possible to access to the statistics and its corresponding input data for dates in the past.

# Note

* If other type of charts are need then the [quickchart.io](https://quickchart.io/) python API will be used (free part).
* [DB Browser for SQLite](https://github.com/sqlitebrowser/sqlitebrowser) can be used to access to the raw data of the [SQLITE DB](data/data.db).
