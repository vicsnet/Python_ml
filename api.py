# !pip install requests
# python3 -m pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://en.wikipedia.org/wiki/Apple_Inc."
headers = {
    "User-Agent": "MyPythonPractice/1.0 (your-email@example.com)"
}


response = requests.get(url, headers=headers)

html_content = response.text
# print(html_content)  # Print the first 500 characters of the HTML content
if response.status_code == 200:
    print("Request successful!")
else:
    print("Failed to retrieve the webpage.")
    
soup = BeautifulSoup(html_content, "html.parser")


headings = [heading.text.strip() for heading in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])]

print(headings)

paragraphs = [paragraph.text.strip() for paragraph in soup.find_all("p")]
print(paragraphs[:5])  # Print the first 5 paragraphs

links = [a['href'] for a in soup.find_all("a", href=True)]
print(links[:5])  # Print the first 5 links

infobox = soup.find('table', class_='infobox')

if infobox:
    rows = infobox.find_all('tr')
    data = {}
    for row in rows:
        header = row.find('th')
        value = row.find('td')
        if header and value:
            data[header.text.strip()] = value.text.strip()
    print("Infobox Data:", data)
    
else:
    print("No infobox found.")
    
    
# convert table to dataframe

table = pd.DataFrame(list(data.items()), columns=['Key', 'Value'])
print(table)

table.to_excel("apple_inc_summary_table.xlsx")