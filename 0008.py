from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "https://www.baidu.com"

html = urlopen(url)

soup = BeautifulSoup(html.read(),'html5lib')
print (soup.body.text)
