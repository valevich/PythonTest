import requests
from bs4 import BeautifulSoup

page = requests.get('https://en.tousecurity.com/free-iptv-links-usa/')
soup = BeautifulSoup(page.text, 'html.parser')

# Remove UNNECESSARY links
#last_links = soup.find(class_='AlphaNav')
#last_links.decompose()

artist_name_list = soup.find(class_='download-attachments')     # Pull all text from the BodyText div
artist_name_list_items = artist_name_list.find_all('a')     # Pull text from all instances of <a> tag within BodyText div

for artist_name in artist_name_list_items:
#    print(artist_name.prettify())
    names = artist_name.contents[0]
#    print(names)
    links = artist_name.get('href')
    print(names)
    print(links)    
    
    

      
    
