from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup


url = 'http://tieba.baidu.com/p/2166231880'
html = urlopen(url)
bsobj = BeautifulSoup(html, 'lxml')
imageTag = bsobj.findAll('img', {'class': "BDE_Image"})
i = 0
for urlTag in imageTag:
    url = urlTag['src']
    # print(url)
    urlretrieve(url, 'img/%s.jpg' % i)
    print('the %s had succeed!' % i)
    i += 1
print('All is done!')
