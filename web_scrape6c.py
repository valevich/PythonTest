import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.iatatravelcentre.com/international-travel-document-news/1580226297.htm')
soup = BeautifulSoup(page.text, 'html.parser')

# Pull all text from the BodyText div
#artist_name_list = soup.find_all(string='values')

# Pull text from all instances of <a> tag within BodyText div
#artist_name_list_items = artist_name_list.find_all('data')

#for artist_name in artist_name_list_item:
#print(artist_name_list)



#for tag in soup.find_all(True):
#    print(tag.a)
# html
# head
# title
# body
# p
# b
# p
# a
# a
# a
# p



titleList = soup.findAll('title')
divList = soup.findAll('div', attrs={ "class" : "middle"})
	
print(divList)