# DOI Open Access Status Crawlers

Dedicated screenscraper to crawl open access status based on DOI of an article.
Made for Wiley content

## How it works

Wiley article page urls can be extended with /epdf. From these EPDF pages, we retrieve the value of the field "'WOL-Article-Access-State'" in the returned HTML source. Currently, this approach only works for articles hosted on onlinelibrary.wiley.com. However, we are very interested in developing similar approaches for other publishers/vendors.

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
