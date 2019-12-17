#!/usr/bin/env python3

# build a collection of data.gov.uk entries

import sys
import glob
import json
import csv

# https://ckan.publishing.service.gov.uk/api/3/action/organization_list
# https://ckan.publishing.service.gov.uk/api/3/action/organization_show?id=kirklees-council&include_datasets=True

cache_dir = "var/data-gov-uk/"

organisation = {}

for path in glob.glob("%s*.json" % (cache_dir)):
    h = json.load(open(path))["result"]

    if "organization" in h:
        organisation[h["organization"]["id"]] = {
            "entry-date": h["organization"]["created"],
            "name": h["organization"]["title"],
        }

fieldnames = ["entry-date", "data-gov-uk-organisation", "name"]

writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames, extrasaction="ignore")
writer.writeheader()

for key, row in organisation.items():
    row['data-gov-uk-organisation'] = key
    writer.writerow(row)
