from newsplease import NewsPlease
import json
url = 'https://www.vanguardia.com/colombia/fiscal-senala-que-no-hay-certeza-de-chuzadas-MG901709'
basepath = '/users/psprao/Downloads/'

article = NewsPlease.from_url(url)

print(article.text)
