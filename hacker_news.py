import requests
import re
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
response = requests.get(url)
content = BeautifulSoup(response.text, "html.parser")

articles = []

for item in content.find_all('tr', class_='athing'):
    # Find the span with class 'titleline'
    title_span = item.find('span', class_='titleline')
    
    if title_span:
        # Extract the 'a' tag inside the span
        item_a = title_span.find('a')
        
        item_link = item_a.get('href') if item_a else None
        item_text = item_a.get_text(strip=True) if item_a else None
    
    # Find the next row, which contains score and comments
    next_row = item.find_next_sibling('tr')

    # Extract the score
    item_score = next_row.find('span', class_='score').get_text(strip=True) if next_row and next_row.find('span', class_='score') else '0 points'

    # Extract the number of comments
    comment_link = next_row.find('a', string=re.compile(r'\d+(&nbsp;|\s)comment(s?)')) if next_row else None
    item_comments = comment_link.get_text(strip=True).replace('\xa0', ' ') if comment_link else '0 comments'

    # Append the article data to the list
    articles.append({
        'link': item_link,
        'title': item_text,
        'score': item_score,
        'comments': item_comments,
    })

# Print the articles
for article in articles:
    print(article)
