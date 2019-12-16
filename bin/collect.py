#!/usr/bin/env python3

# build a collection of data.gov.uk entries

import os
from urllib.parse import urljoin
import requests
import json
import csv

base_url = "https://ckan.publishing.service.gov.uk/api/3/action/"
save_dir = "var/data-gov-uk"
os.makedirs(save_dir, exist_ok=True)


def get(name, url):
    path = os.path.join(save_dir, name + ".json")

    if os.path.isfile(path):
        return json.load(open(path))

    print(url)

    response = requests.get(url)
    with open(path, "wb") as f:
        f.write(response.content)
    return response.json()


packages = get("index", "%spackage_list" % (base_url))["result"]

for package in packages:
    get(package, "%spackage_show?id=%s" % (base_url, package))["result"]
