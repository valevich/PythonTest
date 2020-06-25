import os

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
firstfile = "Y"
tempfile = open("output.txt","w")
prevfile = ""
prevno = 0

for filename in sorted(os.listdir("/Users/henryvalevich/Downloads/Temp/")):
    
    if filename.endswith(".m3u") or filename.endswith(".m3u8"):
        
        fno += 1
        print ("---------------- FILE PROCESSING ----------------")
        with open(filename, 'r',encoding="ISO-8859-1") as searchfile:

            str_idx = int(filename.find("_"))
            newname = (filename[:str_idx] + ".m3u")

            if newname != prevfile:
                if firstfile != "Y":
                    if prevno > 1:
#                        os.rename("output.txt", ("+" + prevfile + ".m3u"))
                        os.rename("output.txt", ("+" + prevfile + ".m3u"))
                    else:    
#                        os.rename("output.txt", ("-" + prevfile + ".m3u"))
                        os.rename("output.txt", ("-" + prevfile + ".m3u"))
                    tempfile.close()
                    tempfile = open("output.txt","w")
                    prevno = 0

            prevfile = newname
            prevno += 1

            for line in searchfile:                        

                if '#EXTM3U' in line:
                    if firstfile == "Y":
                        firstfile = "N"
                        tempfile.writelines(line)
                        print ("First file = " + filename)
                    else:
                        print ("file = " + filename)
                else:         
                    tempfile.writelines(line)

#                if '#EXTINF:' in line:
#                    tempfile.writelines("#EXTGRP:" + xParam + "\n")#

            searchfile.close

            tempfile.writelines ("\n")
            tempfile.writelines ("\n")
            tempfile.writelines("#EXTINF:0,****************\n")
#            tempfile.writelines("#EXTGRP:" + xParam + "\n")
            tempfile.writelines(line)

if prevno > 1:
#    os.rename("output.txt", ("+" + prevfile + ".m3u"))
    os.rename("output.txt", ("+" + prevfile + ".m3u"))
else:    
#    os.rename("output.txt", ("-" + prevfile + ".m3u"))
    os.rename("output.txt", ("-" + prevfile + ".m3u"))

tempfile.close()
print ("---------------------------------------------------")
print ("Total Files: " + str(fno))
print ("---------------------------------------------------")
                    