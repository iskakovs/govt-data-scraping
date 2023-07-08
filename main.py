import requests
from bs4 import BeautifulSoup

# Send a GET request to the webpage containing the HTML table
url = "https://gr5.gosreestr.kz/p/ru/gr-search/search-objects"
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")
