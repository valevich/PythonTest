import os
import vlc
import time
import urllib
import urllib.request
import validators
import socket
from shutil import copyfile

socket.setdefaulttimeout(3)

from multiprocessing import TimeoutError

from datetime import datetime
print ("=====================  START  =====================")
now = datetime.now() # current date and time
date_time = now.strftime("%m%d%Y")

path = "/users/henryvalevich/Downloads/Temp"
retval = os.getcwd()
print ("Current working directory %s" % retval)

os.chdir( path )
retval = os.getcwd()
print ("Directory changed successfully %s" % retval)

fno = 0

for filename in sorted(os.listdir("/Users/henryvalevich/Downloads/Temp/")):
    
    if filename.endswith(".m3u") or filename.endswith(".m3u8"):
        
        fno += 1
        print ("---------------------------------------------------")
        print ("----------  PROCESSING FILE: " + filename + "  -------------")

        with open(filename, 'r') as searchfile:
        
            xOK = 0
            xDead = 0
            xLineCntr = 0
            
            for line in searchfile:                        

                if 'http://' in line:
                    
                    if 'http://blank' in line:
                        continue
                    
                    try:
                
                        xLineCntr += 1
                        if xLineCntr > 5:
                            break
                
                        url = line
                        if not validators.url(url):
                            print ("not valid")

                        code = urllib.request.urlopen(url).getcode()

                        if str(code).startswith('2') or str(code).startswith('3'):
                            print("ok: " + url.rstrip('\r\n'))
#                            print (str(code))
                            xOK += 1
                        else:
                            print("dead1: " + url.rstrip('\r\n'))
#                            print (str(code))
                            xDead += 1


                    except urllib.error.URLError as e: 
                        ResponseData = ''
                        print("dead2: " + url.rstrip('\r\n'))
                        xDead += 1

                    except ValueError: 
                        print("dead3: " + url.rstrip('\r\n'))
                        xDead += 1
                    
#                    except socket.error as e: ResponseData = ''
#                    except socket.timeout as e: ResponseData = ''
#                    except UnicodeEncodeError as e: ResponseData = ''
#                    except http.client.BadStatusLine as e: ResponseData = ''
#                    except http.client.IncompleteRead as e: ResponseData = ''
#                    except urllib.error.HTTPError as e: ResponseData = ''

                    except urllib.error.HTTPError as err:
#                        print(str(err.code) + ": " + url + ' - dead' )
                        print("dead4: " + url.rstrip('\r\n'))
                        xDead += 1

                    except socket.error as err:
                        print("dead5: " + url.rstrip('\r\n'))
                        xDead += 1
#                        sock.close()
                        
#                    except RedisError:
#                        # clean up after any error in on_connect
#                        self.disconnect()
#                        raise

#                    finally:
#                        print ("FINALLY")
                            

                
            print ("---------------------------------------------------")
            print ("Total Valid Links: " + str(xOK))
            print ("Total Dead Links: " + str(xDead))
            
            if xOK == 0:
                copyfile(filename, path + '/Dead/' + filename)
                os.remove(filename)

            searchfile.close


print ("---------------------------------------------------")
print ("Total Files: " + str(fno))
print ("---------------------------------------------------")
                    