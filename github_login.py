import requests
from bs4 import BeautifulSoup



url = "https://github.com/{}"
username = "SamariumCode"


session = requests.Session()
r = session.get(url.format('login'))
content = BeautifulSoup(r.text, 'html.parser')


data = {}

for form in content.find_all('form'):
    for inp in form.select('input[type=hidden]'):
        data[inp.get('name')] = inp.get('value')

data.update({'login': '', 'password': ''})


r = session.post(url.format('session'), data=data)

r = session.get(url.format(username))

content = BeautifulSoup(r.text, 'html.parser')

user_info = content.find_all('span', class_='repo')
for i in user_info:
    print(i.text)
    

print('=' * 80)

repo_url = url.format(username) + '?tab=repositories'

r = session.get(repo_url)

content = BeautifulSoup(r.text, 'html.parser')


info_repos = content.find_all('h3', class_='wb-break-all')


for repo in info_repos:
    repo_name = repo.find('a').get_text(strip=True)
    print(repo_name)


# user_profile_link = content.find('img', class_='avatar avatar-user width-full border color-bg-default').get('src')

# print(user_profile_link)


