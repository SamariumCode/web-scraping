import re
import requests
from bs4 import BeautifulSoup



# User Agent Spoofing
url = "https://bama.ir/"

r = requests.get(url, headers={'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0"})

print(r.text)
