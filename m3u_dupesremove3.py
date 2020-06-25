import os
from operator import itemgetter

from datetime import datetime
print ("=====================  START  =====================")
now = datetime.now() # current date and time
date_time = now.strftime("%m%d%Y")

path = "/users/henryvalevich/Downloads/Temp/"
retval = os.getcwd()
print ("Current working directory %s" % retval)

os.chdir( path )
retval = os.getcwd()
print ("Directory changed successfully %s" % retval)

fno = 0
for filename in sorted(os.listdir("/Users/henryvalevich/Downloads/Temp/")):

    if filename.endswith(".m3u") or filename.endswith(".m3u8"):

        if filename.startswith("+"):
    
            line1 = ""
            line2 = ""
            line3 = ""

            fno += 1
            print ("---------------- FILE PROCESSING ----------------")
            with open(filename, 'r',encoding="ISO-8859-1") as searchfile:


                tempfile = open("tempsort.txt","w")
                for line in searchfile:                        

                    if '#EXTINF:'.casefold() in line.casefold():
                        line1 = line.rstrip()
                        continue

                    if '#EXTGRP:'.casefold() in line.casefold():
                        line2 = line.rstrip()
                        continue

                    if 'http://'.casefold() in line.casefold():
                        line3 = line.rstrip()
                        tempfile.writelines(line1 + "|" + line2 + "|" + line3 + "\n")
                        line1 = ""
                        line2 = ""
                        line3 = ""
            
                tempfile.close
                searchfile.close
                

            pre, ext = os.path.splitext(filename)
            os.rename("tempsort.txt", pre + ".txt")


print ("---------------------------------------------------")
print ("Total Files: " + str(fno))
print ("---------------------------------------------------")
                    