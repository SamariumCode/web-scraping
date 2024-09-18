import requests
from bs4 import BeautifulSoup # type: ignore
import re


url = 'https://en.wikipedia.org/wiki/Mao_Zedong'

response = requests.get(url)

content = BeautifulSoup(response.text, 'html.parser')


# print(content.find_all('h1')) # get all tags h1


# print(content.find('h1').attrs) # get first tag h1, get attributes tag h1


# print(content.find('h1').text) # get first tag h1, get text tag h1


# print(content.find('h1').name) # name tag (return value 'h1')


# print(content.findAll(['h1', 'h2'])) # get all tag h1, h2


# print(content.find(attrs={'id':'n-mainpage-description'})) # get tag with id 'n-mainpage-description'


# print(content.find('div', class_='vector-menu mw-portlet mw-portlet-navigation')) # get tag with class 'vector-menu mw-portlet mw-portlet-navigation and tag 'div'


# print(content.find_all('h2', limit=5)) # get all tag 'h2' and limit result to 5


# print(content.find('h2').get('class')) # get first tag 'h2', get attribute 'class'



# use modele regular expression

# print(content.find_all(re.compile('^a')))


# print(content.select('li > a[title="Benjamin Tucker"]')) # get all tag 'a' with attribute 'title' and text 'Benjamin Tucker'


# print(content.prettify())


# print(content.title.text)

# print(content.title.parent.name)

# print(content.p)

# print(content.p['class'])




# Brnach amir created to get the first paragraph text

# Branch main content