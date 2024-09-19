import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

# URL of the page to fetch
url = "https://www.varzesh3.com/football/league/6/لیگ-برتر-ایران"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    content = BeautifulSoup(response.text, 'html.parser')
    
    # Find the specific table by class
    table = content.find('table', class_="league-standing football-standing")
    
    if table:
        # Extract table headers
        headers = [th.get_text(strip=True).replace('\u200c', '') for th in table.find('thead').find('tr').find_all('th')]
        
        # Extract numerical data
        data = []
        tbody = table.find('tbody')
        if tbody:
            for row in tbody.find_all('tr'):
                row_data = [td.get_text(strip=True).replace('\u200c', '') for td in row.find_all('td')]
                data.append(row_data)
        
        # Define column alignment: 'right' for numeric, 'left' for text
        colalign = ['right'] * len(headers)  # Default all to 'right'
        # Adjust specific columns to 'left' if they are text-based (e.g., team names)
        # Example: Setting the second column (team names) to 'left'
        colalign[1] = 'left'
        
        # Print headers and formatted data using tabulate with custom alignment
        print(tabulate(data, headers=headers, tablefmt='grid', colalign=colalign))
    else:
        print("Table with the specified class not found.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
