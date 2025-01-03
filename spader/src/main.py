import requests

link = 'https://browser-info.ru/'
responce = requests.get(link).text

##print(responce)
with open('testPage.html', 'w', encoding='utf-8') as file:
    file.write(responce)
