import requests
from requests.auth import HTTPBasicAuth


catalog_url = "https://fairicube.github.io/data-requests/catalog.json"
post_url = "https://stacapi-write.eoxhub.fairicube.eu/collections/index/items"
index_catalog = requests.get(catalog_url).json()
for link in index_catalog["links"]:
    if link["rel"] == "item":
        json_body = requests.get(link["href"]).json()
        response = requests.post(
            url=post_url, json=json_body,
            auth=HTTPBasicAuth(
                'user', 'password'))
