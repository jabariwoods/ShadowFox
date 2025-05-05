import requests
from bs4 import BeautifulSoup
import csv

# Error handling wrapper
def safe_scrape(url):
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')
    except (requests.exceptions.RequestException, ConnectionError) as e:
        print(f"Error fetching {url}: {e}")
        return None

# Data extraction
soup = safe_scrape("https://www.shadowfox.in/")
data = []
if soup:
    for item in soup.select('.product-item'):
        try:
            data.append({
                'name': item.find('h3').text.strip(),
                'price': item.find('span', class_='price').text
            })
        except AttributeError as e:
            print(f"Parsing error: {e}")

# Save to CSV
with open('products.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'price'])
    writer.writeheader()
    writer.writerows(data)
