import requests


url = 'https://www.mongard.ir/'

response = requests.get(url)

# print(response.url)
# print(response.status_code)
# print(response.request)
# print(response.request.headers)
# print(response.reason)
# print(response.headers)
# print(dir(response))

print(response.text)