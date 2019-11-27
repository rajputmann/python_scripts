import bs4
import requests
import sys  
reload(sys)  
sys.setdefaultencoding('utf-8')
url = "https://en.wikipedia.org/wiki/List_of_FIFA_country_codes"
data = requests.get(url)
soup = bs4.BeautifulSoup(data.text, 'html.parser')
#print (soup.prettify())
with open ('aajnew.txt',"w")as f:
    for para in soup.find_all ("p"):
        #print (para.text)
        f.write(para.text+'\n'+ " ")
