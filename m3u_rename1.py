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
i = 0
max = 21

tempfile = open("output.txt","w")

for filename in os.listdir("/Users/henryvalevich/Downloads/Temp/"):
    
    if filename.endswith(".m3u") or filename.endswith(".m3u8"):
        
        fno += 1
        renam = "no"
        print ("---------------- FILE PROCESSING: " + filename + " ----------------")
        with open(filename, 'r') as searchfile:

            for line in searchfile:
        
                if i < max:
                    i += 1
                    tempfile.writelines(line)
                else:
                    i = 0
                    break
                                
                if 'http://' in line:
                    oldname = line.replace("http://","")
                    oldname = oldname.replace(":","-")
                    str_idx = int(oldname.find("/"))
                    newname = (oldname[:str_idx] + "_" + str(fno) + "_" + date_time + ".m3u")
                    renam = "yes"

            if renam == "yes":
                tempfile.writelines("#EXTINF:0,-------------- " + newname + " --------------\r\n")
                tempfile.writelines("http://-----------------------------\r\n")
                print ("filename: " + filename)
                print ("newname: " + newname)
                os.rename(filename, newname)

            searchfile.close

os.rename("output.txt", ("-output_" + date_time + ".m3u"))
tempfile.close()
print ("---------------------------------------------------")
print ("Total Files: " + str(fno))
print ("---------------------------------------------------")
                    