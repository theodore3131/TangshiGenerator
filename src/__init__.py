import urllib3
from bs4 import BeautifulSoup
import certifi

file = open('../data/poem', "wb+")
http = urllib3.PoolManager(
     cert_reqs='CERT_REQUIRED',
     ca_certs=certifi.where())

url = 'http://so.gushiwen.org'
r = http.request('GET', url+'/gushi/tangshi.aspx')

soup = BeautifulSoup(r.data, 'html.parser')

main = soup.find('div',class_="main3")

content = main.find('div',class_="left")

for link in content.find_all('a'):
    next = http.request('GET', url+link.get('href'))
    soup1 = BeautifulSoup(next.data, 'html.parser')
    poem = soup1.find('div',class_="contson")
    file.write(poem.get_text().encode('utf-8'))

