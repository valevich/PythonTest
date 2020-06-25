# Import libraries
#import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import re

#url = 'http://web.mta.info/developers/turnstile.html'
#response = requests.get(url)
#soup = BeautifulSoup(response.text, "html.parser")
#
#for i in range(36,len(soup.findAll('a'))+1): #'a' tags are for links
#    one_a_tag = soup.findAll('a')[i]
#    link = one_a_tag['href']
#    download_url = 'http://web.mta.info/developers/'+ link
#    urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:]) 
#    time.sleep(1) #pause the code for a sec
    
    


url = "https://en.tousecurity.com/iptv-links-m3u-list-10-01-2020/amp/"                     # ok
#url = urllib.request.urlopen("http://iptv.filmover.com/category/uk/")                        # no
#url = urllib.request.urlopen("http://iptv.filmover.com/iptv-m3u-playlist-07-jan-2020/")      # no
#url = urllib.request.urlopen("https://en.tousecurity.com/free-iptv-links-usa/amp/")          # forbidden
#url = urllib.request.urlopen("https://en.tousecurity.com/iptv-free-uk/amp/")                 # forbidden
#url = "https://www.iptvm3uts.us/2019/06/usa-free-iptv-today-new-m3u-kodi.html/"              # no
#url = "view-source:https://www.iptvsource.com/usa-free-iptv-source-lists-10-01-20/"          # no

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html_page = urllib.request.urlopen(req).read().decode('utf-8')

#soup = BeautifulSoup(html_page,features="lxml")
#for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
#    print (link.get('href'))

soup = BeautifulSoup(html_page,features="lxml")
for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    href = link.get('href')
    if any(href.endswith(x) for x in ['=m3u','=m3u8']):
#    if any(href.endswith(x) for x in ['=download']):
        print (href)

