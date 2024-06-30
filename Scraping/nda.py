from bs4 import BeautifulSoup
import requests
import pandas as pd

# URL
url = 'https://en.wikipedia.org/wiki/List_of_National_Democratic_Alliance_members'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table', class_='wikitable')

headers = table.find_all('th')
header_titles = [header.text.strip() for header in headers]


political_party_index = header_titles.index('Political party')
political_parties = []

for row in table.find_all('tr')[1:]:
    columns = row.find_all('td')
    if len(columns) > political_party_index:
        political_party = columns[political_party_index].text.strip()
        political_parties.append(political_party)

df = pd.DataFrame(political_parties, columns=['Political Party'])
print(df)

output_file = 'NDA_parties.xlsx'
df[:39].to_excel(output_file, index=False)
print(f"Saved the data to {output_file}")
