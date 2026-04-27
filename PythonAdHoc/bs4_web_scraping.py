import requests
import json
from bs4 import BeautifulSoup
from pprint import pprint

url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
headers = {
    "User-Agent": "Mozilla/5.0 (compatible; MyBot/1.0; +https://example.com/bot)"
}

res = requests.get(url, headers=headers)

#data = json.dumps(res.__dict__, indent=4)

#pprint(res.__dict__)
pprint(res.__dir__())

#print(f"res.status_code: {res.status_code}\n")
#print(f"res: {res}\n")
#print(f"data: {data}\n")
#print(res.text[:500])  # preview first 500 characters
