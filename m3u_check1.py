import os
import vlc
import time
import urllib
import urllib.request
import validators

from datetime import datetime
now = datetime.now() # current date and time
date_time = now.strftime("%m%d%Y")

i = 0

#url = 'http://aska.ru-hoster.com:8053/autodj'
#url = 'http://rb-group-server.com:25461/rachidx48/exchange_skype/3785'
#url = 'http://beastiptv.tv:25461/live/Shauna12/Shauna12/6954.m3u8'
url = 'http://moiptvhls-i.akamaihd.net/hls/live/652313/HQs/chunklist.m3u8'

if not validators.url(url):
	print ("not valid")

x = 0
try:
#    urllib.request.urlretrieve(url)
	code = urllib.request.urlopen(url).getcode()
	if str(code).startswith('2') or str(code).startswith('3'):
	    print('Stream is working')
	else:
	    print('Stream is dead')
except urllib.error.HTTPError as err:
    print(err.code)
    x = 1

print (x)

#code = urllib.request.urlopen(url).getcode()
#if str(code).startswith('2') or str(code).startswith('3'):
#    print('Stream is working')
#else:
#    print('Stream is dead')

##instance = vlc.Instance('--input-repeat=-1', '--fullscreen')
#instance = vlc.Instance('--input-repeat=-1', '--no-video')
#player=instance.media_player_new()
#media=instance.media_new(url)
#player.set_media(media)

#player.play()
#time.sleep(3)
#state = str(player.get_state())

#if state == "vlc.State.Error" or state == "State.Error":
#    print ('Stream is dead. Current state = '.format(state))
#    player.stop()
#else:
#    print ('Stream is working. Current state = {}'.format(state))
#    player.stop()