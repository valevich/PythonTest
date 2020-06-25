import os
import sys

from datetime import datetime
print ("=====================  START  =====================")
now = datetime.now() # current date and time
date_time = now.strftime("%m%d%Y")

#try:
#    sys.argv[1]
#except IndexError:
#    print "Parameter is missing!"
#    sys.exit() 
#
#xParam = sys.argv[1]
#print ("Group Parameter %i: %s" % (1, sys.argv[1]))

path = "/users/henryvalevich/Downloads/Temp"
retval = os.getcwd()
print ("Current working directory %s" % retval)

os.chdir( path )
retval = os.getcwd()
print ("Directory changed successfully %s" % retval)

fno = 0
#firstfile = "Y"
#tempfile = open("output.txt","w")
prevfile = ""

for filename in sorted(os.listdir("/Users/henryvalevich/Downloads/Temp/")):
    
    if filename.endswith(".m3u") or filename.endswith(".m3u8"):
        
        fno += 1
        print ("---------------- FILE PROCESSING ----------------")
        with open(filename, 'r') as searchfile:

            str_idx = int(filename.find("_"))
            newname = (filename[:str_idx] + ".m3u")
#            print ("Pre: " + prevfile)
#            print ("New: " + newname)


            if newname != prevfile:
                os.rename(filename, ("+" + newname))
                print ("1: " + newname)
            else:
                os.rename(filename, ("-" + newname + str(fno)))
                print ("2: " + newname)

            prevfile = newname


#            for line in searchfile:                        
#
#                if '#EXTM3U' in line:
#                    if firstfile == "Y":
#                        firstfile = "N"
#                        tempfile.writelines(line)
#                        print ("First file = " + filename)
#                    else:
#                        print ("file = " + filename)
#                else:         
#                    tempfile.writelines(line)
#
#                if '#EXTINF:' in line:
#                    tempfile.writelines("#EXTGRP:" + xParam + "\n")#
#
#            searchfile.close
#
#            tempfile.writelines ("\n")
#            tempfile.writelines ("\n")
#            tempfile.writelines("#EXTINF:0,****************\n")
#            tempfile.writelines("#EXTGRP:" + xParam + "\n")
#            tempfile.writelines(line)


#os.rename("output.txt", ("-output_" + date_time + ".m3u"))
#tempfile.close()
print ("---------------------------------------------------")
print ("Total Files: " + str(fno))
print ("---------------------------------------------------")
                    