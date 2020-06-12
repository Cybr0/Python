import urllib.request
from bs4 import BeautifulSoup

request = urllib.request.urlopen('https://kinohit.uz/')
html = request.read()
# print(html)
soup = BeautifulSoup(html, 'html.parser')
# print(soup)
news = soup.find_all('a', class_="popover-dismissible-serial")
print(news)
results = []
for item in news:
    title = item.find('div', class_='data-original-title')
    print(title)
    desc = None
    href = None

# with open('you.html', 'w') as f:
#     f.write(news)

'''
TODO: хз нужно будет подумать....
'''