import os
import urllib

from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
from urllib.error import HTTPError


#URL = 'http://213.152.172.67:25461/get.php?username=sourcegermanypro2&password=0626674936&type=m3u'
URL = 'http://iptv.filmover.com/iptv-m3u-playlist-07-jan-2020/'
OUTPUT_DIR = '/Users/henryvalevich/Downloads/'  # path to output folder, '.' or '' uses current folder

u = urlopen(URL)
try:
    html = u.read().decode('utf-8')
finally:
    u.close()

soup = BeautifulSoup(html, "html.parser")
for link in soup.select('a[href^="http://"]'):
    href = link.get('a')
    if not any(href.endswith(x) for x in ['.m3u','.m3u8']):
        continue

filename = os.path.join(OUTPUT_DIR, href.rsplit('/', 1)[-1])

# We need a https:// URL for this site
href = href.replace('http://','https://')

try:
    print("Downloading %s to %s..." % (href, filename) )
    urlretrieve(href, filename)
    print("Done.")
except urllib.error.HTTPError as err:
    if err.code == 404:
#        continue
        print ("error")