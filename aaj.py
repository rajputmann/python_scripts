import requests
import bs4
import sys  
reload(sys)  
sys.setdefaultencoding('utf-8')
from selenium import webdriver
url = "https://www.tiktok.com/"
data = requests.get(url)
soup = bs4.BeautifulSoup(data.text, 'html.parser')
#print (soup.prettify())
    #print(para.text)
for links in soup.find_All ('a'):
   links = links.get('href')
   print (links)
        #f.write(para.text+'\n')