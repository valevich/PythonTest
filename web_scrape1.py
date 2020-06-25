import os
import urllib
import urllib.request

#url = "https://www.livesoccertv.com/schedules/"
url = "https://www.iatatravelcentre.com/international-travel-document-news/1580226297.htm"


# Open the URL as Browser, not as python urllib
page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
infile=urllib.request.urlopen(page).read()
data = infile.decode('ISO-8859-1') # Read the content as string decoded with ISO-8859-1

print(data) # Print the data to the screen
