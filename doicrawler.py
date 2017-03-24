#!/usr/bin/env python

import requests
import re
import argparse
import time


parser = argparse.ArgumentParser(description="Find open access state from DOI on wiley")
parser.add_argument("--filename", "-f", help='Give the filename with the DOIs')
parser.add_argument("--timeout", "-t", type=int, help="Timeout option to prevent flooding the wiley servers too much", default=5)

args = parser.parse_args()


articles = open(args.filename, 'r');
for id in articles:
    time.sleep(args.timeout)
    id = str(id).rstrip()
    url = "http://onlinelibrary.wiley.com/doi/" + id + "/epdf"
    r = requests.get(url)
    if (r.status_code == 200):
        access = re.search("'WOL-Article-Access-State': '(.*)',", r.content)
        if access:
            print id + " : " + access.group(1)
        else:
            print id + ": Access not specified"
    else:
        print id + " : Article not found"
