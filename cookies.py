import requests


url = "https://gitlab.com/"


r = requests.get(url, cookies={'remember_user_token': 'your_token_here'})


print(r.text)