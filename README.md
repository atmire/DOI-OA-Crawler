# DOI-OA-Crawler
Scripting and tooling to crawl open access status based on DOI of an article.

## Requirements

Python >2.7

Request library for python, install with pip:

`pip install requests`

## Usage

Create a file with the DOI's in the following format:

```
10.1046/j.1365-3040.2000.00558.x
10.1002/app.1973.070170320
10.1111/jbl.12013
```

Run the code with `python doicrawler.py -f {filename with DOI's} -t {timeout}`

### Arguments

```
-h, --help            show this help message and exit
--filename FILENAME, -f FILENAME
                      Give the filename with the DOIs
--timeout TIMEOUT, -t TIMEOUT
                      Timeout option to prevent flooding the wiley servers
                      too much
```
