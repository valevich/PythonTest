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
prevcol3 = ""
d=[]

with open('tempsort.txt','r') as infile:
    fno += 1
    for line in infile.readlines():
        data = line.strip().split('|')
        d.append(data)
d.sort(key=itemgetter(2))                 #sort the list `d` with the 2 item(3th column) of your sublist.

with open('outfile1.txt','w') as outfile:
    for line in d:
        xline = ('|'.join(line)+'\n')
        str_idx1 = int(xline.find("|"))
        str_idx2 = int(xline.find("http://"))
        col1 = (xline[:str_idx1])
        col2 = (xline[str_idx1+1:str_idx2-1])
        col3 = (xline[str_idx2:])
        if col3 != prevcol3:
            outfile.writelines(col1 + '|' + col2 + '|' + col3)
        prevcol3 = col3        

d=[]
with open('outfile1.txt','r') as infile:
    fno += 1
    for line in infile.readlines():
        data = line.strip().split('|')
        d.append(data)
d.sort(key=itemgetter(0))                 #sort the list `d` with the 2 item(3th column) of your sublist.

with open('outfile2.txt','w') as outfile:
    for line in d:
        xline = ('|'.join(line)+'\n')
        str_idx1 = int(xline.find("|"))
        str_idx2 = int(xline.find("http://"))
        col1 = (xline[:str_idx1])
        col2 = (xline[str_idx1+1:str_idx2-1])
        col3 = (xline[str_idx2:])
        outfile.writelines(col1+'\n')
        outfile.writelines(col2+'\n')
        outfile.writelines(col3)
#            print (col1)
#            print (col2)
#            print (col3)
#        prevcol3 = col3        
#os.rename("outfile.txt", "outfile" + fno + ".txt")



print ("---------------------------------------------------")
print ("Total Files: " + str(fno))
print ("---------------------------------------------------")
                    