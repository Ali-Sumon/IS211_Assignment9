import requests
import pandas as pd
from bs4 import BeautifulSoup


url = "https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table with class wikitable
    table = soup.find('table', {'class': 'wikitable'})

    if table:
        rows = table.find_all('tr')

        for row in rows:
            columns = row.find_all(['th', 'td'])
            for column in columns:
                print(column.get_text(), end='\t')
            print()  # Move to the next line after each row
    else:
        print("No table found on the page.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
