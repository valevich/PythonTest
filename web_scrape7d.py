import requests
import urllib.request
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
from datetime import datetime
import os
import re

os.system('cls||clear')
print ("")
print ("=====================  START  =====================")
now = datetime.now() # current date and time
#date_time = now.strftime("%m%d%Y")
date_time = now.strftime("%d-%m")
print ("Today: " + date_time)
path = "/users/henryvalevich/Downloads/Temp"
retval = os.getcwd()
print ("Current working directory %s" % retval)
os.chdir( path )
retval = os.getcwd()
print ("Directory changed successfully %s" % retval)


def download_function(url):

#    url = "https://en.tousecurity.com/free-iptv-links-usa/"
#    url = "https://en.tousecurity.com/iptv-free-uk/"

    print ("Processing URL: " + url)

    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent,} 
    request=urllib.request.Request(url,None,headers) #The assembled request
    response = urllib.request.urlopen(request)
    data = response.read() # The data u need


    soup = BeautifulSoup(data, 'html.parser')
    artist_name_list = soup.find(class_='download-attachments')     # Pull all text from the BodyText div
    artist_name_list_items = artist_name_list.find_all('a')     # Pull text from all instances of <a> tag within BodyText div
    
    x = 0
    for artist_name in artist_name_list_items:
        names = artist_name.contents[0]
        links = artist_name.get('href')
#        print(names)
#        print(links)

        date_strings = re.findall("(\d+\-\w+)", names)
        for i in date_strings:
            if date_time <= i:
                x += 1
                print(names)
                r = requests.get(links)
                with open(names + '.m3u', 'wb') as outfile:
                    outfile.write(r.content)

    print ("--Total Files Downloaded: " + str(x))


#==========================================  MAIN LOGIC  ==========================================

if __name__ == "__main__":
    
    url = "https://en.tousecurity.com/free-iptv-links-usa/"
    download_function(url)     

    url = "https://en.tousecurity.com/iptv-free-uk/"
    download_function(url)     

