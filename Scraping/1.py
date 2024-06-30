from bs4 import BeautifulSoup
import requests
import pandas as pd
import os

# Base URL
base_url = 'https://results.eci.gov.in/PcResultGenJune2024/'

# URL of the main page
main_page_url = base_url + 'index.htm'
response = requests.get(main_page_url)

if response.status_code != 200:
    print(f"Failed to retrieve the main page. Status code: {response.status_code}")
    exit()

soup = BeautifulSoup(response.text, 'html')

# Extract all relevant table URLs
table_links = soup.find_all('a', href=True, string=True)
table_urls = [base_url + link['href'] for link in table_links if 'partywisewinresultState' in link['href']]

# Output directory
output_directory = r'C:\Users\hp\OneDrive\Desktop\kvtask'
output_file = os.path.join(output_directory, 'election_results.xlsx')

# Initialize an empty DataFrame for all combined data
combined_df = pd.DataFrame()

# List of parties (to match with the table URLs in order)
party = [
    'Bharatiya Janata Party - BJP',
    'Indian National Congress - INC',
    'Samajwadi Party - SP',
    'All India Trinamool Congress - AITC',
    'Dravida Munnetra Kazhagam - DMK',
    'Telugu Desam - TDP',
    'Janata Dal  (United) - JD(U)',
    'Shiv Sena (Uddhav Balasaheb Thackrey) - SHSUBT',
    'Nationalist Congress Party – Sharadchandra Pawar - NCP',
    'Shiv Sena - SHS',
    'Lok Janshakti Party(Ram Vilas) - LJPRV',
    'Yuvajana Sramika Rythu Congress Party - YSRCP',
    'Rashtriya Janata Dal - RJD',
    'Communist Party of India  (Marxist) - CPI(M)',
    'Indian Union Muslim League - IUML',
    'Aam Aadmi Party - AAAP',
    'Jharkhand Mukti Morcha - JMM',
    'Janasena Party - JnP',
    'Communist Party of India  (Marxist-Leninist)  Liberation - CPI(ML)',
    'Janata Dal  (Secular) - JD(S)',
    'Viduthalai Chiruthaigal Katchi - VCK',
    'Communist Party of India - CPI',
    'Rashtriya Lok Dal - RLD',
    'Jammu & Kashmir National Conference - JKN',
    'United People’s Party, Liberal - UPPL',
    'Asom Gana Parishad - AGP',
    'Hindustani Awam Morcha (Secular) - HAMS',
    'Kerala Congress - KEC',
    'Revolutionary Socialist Party - RSP',
    'Nationalist Congress Party - NCP',
    'Voice of the People Party - VOTPP',
    'Zoram People’s Movement - ZPM',
    'Shiromani Akali Dal - SAD',
    'Rashtriya Loktantrik Party - RLTP',
    'Bharat Adivasi Party - BHRTADVSIP',
    'Sikkim Krantikari Morcha - SKM',
    'Marumalarchi Dravida Munnetra Kazhagam - MDMK',
    'Aazad Samaj Party (Kanshi Ram) - ASPKR',
    'Apna Dal (Soneylal) - ADAL',
    'AJSU Party - AJSUP',
    'All India Majlis-E-Ittehadul Muslimeen - AIMIM',
    'Independent - IND'
]

# Iterate over each URL and scrape data
for idx, table_url in enumerate(table_urls):
    print(f"Scraping {table_url}")
    
    # Request the page
    page = requests.get(table_url)
    soup = BeautifulSoup(page.text, 'html')
    
    # Find the table
    table = soup.find('table', class_='table table-striped table-bordered')
    
    # Extract the table headers
    titles = table.find_all('th')
    table_titles = [title.text.strip() for title in titles]
    
    # Create a temporary DataFrame for the current party
    df = pd.DataFrame(columns=table_titles)
    
    # Extract table rows
    column_data = table.find_all('tr')
    
    # Party name
    party_name = party[idx]
    
    # Iterate over each row in the table (skipping the header row)
    for row in column_data[1:]:
        row_data = row.find_all('td')
        individual_row_data = [data.text.strip() for data in row_data]
        
        # Add the data to the DataFrame
        df.loc[len(df)] = individual_row_data
    
    # Add a column for the party name
    df['Party'] = party_name.split(' - ')[0]
    
    # Append to the combined DataFrame
    combined_df = pd.concat([combined_df, df], ignore_index=True)

# Save the combined DataFrame to a single Excel file
combined_df.to_excel(output_file, index=False)
print(f"Saved all data to {output_file}")