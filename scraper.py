import requests
from bs4 import BeautifulSoup

name = "GoPro HERO 7 Black"
URL = "https://www.amazon.com/GoPro-HERO7-Black-Waterproof-Streaming-Stabilization/dp/B07GDGZCCH/ref=sr_1_3?keywords=gopro+hero+7&qid=1563165487&s=gateway&sr=8-3"

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())