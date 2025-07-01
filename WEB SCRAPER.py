import requests
from bs4 import BeautifulSoup
import csv

# Target URL
URL = "http://books.toscrape.com/"

# Send a GET request
response = requests.get(URL)

# Parse HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Find all book containers
books = soup.find_all('article', class_='product_pod')

# Open CSV file for writing
with open('books.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    # Write header
    writer.writerow(['Title', 'Price'])

    # Loop through each book and extract data
    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        writer.writerow([title, price])

print("Scraping complete. Data saved to books.csv.")
