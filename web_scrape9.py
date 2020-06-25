import requests
import urllib.request
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
from datetime import datetime
import os
import re

os.system('cls||clear')
print ("=================================================================")
print ("=========  DOWNLOAD FROM: https://www.dailym3uiptv.com  =========")
print ("=================================================================")

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

found = False

def download_function(url,tagid):

    print ("Processing URL: " + url)

    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent,} 
    request=urllib.request.Request(url,None,headers) #The assembled request
    response = urllib.request.urlopen(request)
    data = response.read() # The data u need


    soup = BeautifulSoup(data, 'html.parser')
#    down_list = soup.find(id='aim26903022384055098734')         # Pull all text from the BodyText div
    down_list = soup.find(id=tagid)                             # Pull all text from the BodyText div
    down_list_items = down_list.find_all('a')                   # Pull text from all instances of <a> tag within BodyText div
    
#    f = open("Backup/---m3u_downloads.txt", "a")
    x = 0
    for down in down_list_items:
        names = down.contents[0]
        names = names.replace("Download ","")
        links = down.get('href')
#        print(names)
#        print(links)

        x += 1
        print(names)
        r = requests.get(links)
        with open(names + '.m3u', 'wb') as outfile:
            outfile.write(r.content)

    print ("--Total Files Downloaded: " + str(x))

'''
        date_strings = re.findall("(\d+\-\w+)", names)
        for i in date_strings:
            if date_time <= i:
                if check(links):
                    print ("Already Downloaded...Exiting!")
                    continue
                else:
                    print ("Downloading..." + links)
                x += 1
                print(names)
                r = requests.get(links)
                with open(names + '.m3u', 'wb') as outfile:
                    outfile.write(r.content)
                f.write(links + "," + names + '\n')

    print ("--Total Files Downloaded: " + str(x))
    f.close()
'''



def check(txt):
    with open("Backup/---m3u_downloads.txt") as dataf:
        return any(txt in line for line in dataf)




#==========================================  MAIN LOGIC  ==========================================

if __name__ == "__main__":
    
    url = "https://www.dailym3uiptv.com/p/get-sports-iptv-links.html"
    tagid = "aim26903022384055098734"
    download_function(url,tagid)     

    url = "https://www.dailym3uiptv.com/p/get-woldwide-iptv-links.html"
    tagid = "aim26914974246734341312"
    download_function(url,tagid)     

    url = "https://www.dailym3uiptv.com/p/get-usa-iptv.html"
    tagid = "aim26881774670770946201"
    download_function(url,tagid)     

    url = "https://www.dailym3uiptv.com/p/get-uk-iptv-links.html"
    tagid = "aim23100701974655500321"
    download_function(url,tagid)     





