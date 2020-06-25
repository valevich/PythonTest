import os

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
line1 = ""
line2 = ""

for filename in sorted(os.listdir("/Users/henryvalevich/Downloads/Temp/")):
    
    if filename.endswith(".m3u") or filename.endswith(".m3u8"):

        if filename.startswith("+"):
        
            fno += 1
            print ("---------------- FILE PROCESSING ----------------")
            with open(filename, 'r',encoding="ISO-8859-1") as searchfile:

                tempfile = open("tempsort.txt","w")
                line1 = ""
                line2 = ""

                for line in searchfile:                        

                    if '#EXTINF:'.casefold() in line.casefold():
                        line1 = line.rstrip()
                        continue

                    if '#EXTGRP:'.casefold() in line.casefold():
                        line2 = line.rstrip()
                        continue

                    if 'http://'.casefold() in line.casefold():
                        line3 = line.rstrip()
                        line3.ljust(75, '0')
                        tempfile.writelines(line3.ljust(75, ' ') + "|1|" + line1 + "|2|" + line2 + "\n")
                        line1 = ""
                        line2 = ""
                
                searchfile.close
                
                

    tempfile.close()


tempfile = open("sorted.txt","w")
newline = ''

prev = None
prevline = None
for line in (open('tempsort.txt')):
    col0 = line[0:75].strip()
    if prev is not None and not col0.startswith(prev):
        str_idx1 = int(prevline.find("|1|"))
        str_idx2 = int(prevline.find("|2|"))
        col1 = (prevline[str_idx1+3:str_idx2])
        col2 = (prevline[str_idx2+3:])
        tempfile.writelines(col1.rstrip() + "\n")
        tempfile.writelines(col2.rstrip() + "\n")
        tempfile.writelines(prev.rstrip() + "\n")
    prev = col0
    prevline = line
if prev is not None:
    str_idx1 = int(line.find("|1|"))
    str_idx2 = int(line.find("|2|"))
    col1 = (line[str_idx1+3:str_idx2])
    col2 = (line[str_idx2+3:])
    tempfile.writelines(col1.rstrip() + "\n")
    tempfile.writelines(col2.rstrip() + "\n")
    tempfile.writelines(prev.rstrip() + "\n")

#    os.rename("sorted.txt", ("sorted" + filename))
#    os.rename("tempsort.txt", ("tempsort" + filename))
#    copyfile("tempsort.txt", "tempsort-" + filename)
  

print ("---------------------------------------------------")
print ("Total Files: " + str(fno))
print ("---------------------------------------------------")
                    