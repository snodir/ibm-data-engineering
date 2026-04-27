import requests
from bs4 import BeautifulSoup
import json
import pprint

# Specify the URL of the webpage you want to scrape
# url = 'https://en.wikipedia.org/wiki/IBM'

# Send an HTTP GET request to the webpage
# response = requests.get(url)

# Store the HTML content in a variable
# html_content = response.text

# Create a BeautifulSoup object to parse the HTML
# soup = BeautifulSoup(html_content, 'html.parser')

# Display a snippet of the HTML content
# print(html_content[:500])


url = "https://en.wikipedia.org/api/rest_v1/page/summary/IBM"
headers = {
    "User-Agent": "MyAppName/1.0 (https://example.com/contact)"
}
response = requests.get(url, headers=headers)

data = response.json()

print(json.dumps(data, indent=4))
print(f"\nresponse: {response}\n")
print(f"type(response): {type(response)}\n")
print(f"dir(response): {dir(response)}\n")

print(f"response.__dict__: {response.__dict__}\n")
print(f"data: {data}\n")
print(f"type(data): {type(data)}\n")
# print(data["title"], "-", data["extract"])
