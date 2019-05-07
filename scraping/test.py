from newsplease import NewsPlease
import json
url = 'https://www.rt.com/news/203203-ukraine-russia-troops-border/'
basepath = '/users/psprao/Downloads/'

article = NewsPlease.from_url(url)

with open(basepath + article.language + '.json', 'w') as outfile:
    json.dump(article, outfile, indent=4, sort_keys=True)
