import os
import re

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


#==========================================  DUPESMERGE FUNCTION  ==========================================
def dupesmerge_function():

    fno = 0
    firstfile = "Y"
    prevname = ""
    d=[]

    m3ufiles = [f for f in os.listdir(path) if re.search(r'.*\.(m3u|m3u8)$', f)]

    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("~~~~~~~~~~~~~~  BEGIN PROCESS: " + "(dupesmerge_function) ~~~~~~~~~~~~~~")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    for filename in sorted(os.listdir(path)):
    
        if filename.endswith(".m3u") or filename.endswith(".m3u8"):
        
            fno += 1

            with open(filename, 'r',encoding="ISO-8859-1") as searchfile:

                str_idx = int(filename.find("-"))
                xname = (filename[:str_idx])

                if firstfile == "Y":
                    firstfile = "N"
                    prevname = xname
                    for line in searchfile.readlines():
                        data = line.strip()
                        d.append(data)
                    os.remove(filename)
                    continue

                if xname == prevname:
                    for line in searchfile.readlines():
                        data = line.strip()
                        d.append(data)
                    os.remove(filename)
                    continue
                
                with open('outfile.txt','w') as outfile:
                    for xline in d:
                        outfile.writelines(xline+'\n')
                    d=[]

                for line in searchfile.readlines():
                    data = line.strip()
                    d.append(data)
                print ("file = " + prevname)
                os.rename("outfile.txt", ("+-" + prevname + ".m3u"))
                prevname = xname
        
            os.remove(filename)
    
    with open('outfile.txt','w') as outfile:
        for xline in d:
            outfile.writelines(xline+'\n')
        d=[]
    print ("file = " + prevname)
    os.rename("outfile.txt", ("+-" + prevname + ".m3u"))
    prevname = xname

    print ("---------------------------")
    print ("Total Files: " + str(fno))
    print ("---------------------------")
    print ("")



#==========================================  DUPESREMOVE1 FUNCTION  ==========================================
def dupesremove1_function():

    fno = 0

    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("~~~~~~~~~~~~~~  BEGIN PROCESS: " + "(dupesremove1_function) ~~~~~~~~~~~~~~")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for filename in sorted(os.listdir(path)):
    
        if filename.endswith(".m3u") or filename.endswith(".m3u8"):
        
            if filename.startswith("+"):
    
                line1 = ""
                line2 = ""
                line3 = ""

                fno += 1
                
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
                            if not line2.rstrip():
                                line2 = "#EXTGRP:FOOTBALL"
                            tempfile.writelines(line1 + "|" + line2 + "|" + line3 + "\n")
                            line1 = ""
                            line2 = ""
                            line3 = ""
            
                    tempfile.close
                    searchfile.close
                    print ("file = " + filename)
                 

                pre, ext = os.path.splitext(filename)
                os.rename("tempsort.txt", pre + ".txt")



    print ("---------------------------")
    print ("Total Files: " + str(fno))
    print ("---------------------------")
    print ("")



#==========================================  DUPESREMOVE2 FUNCTION  ==========================================
def dupesremove2_function():
    
    from operator import itemgetter

    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("~~~~~~~~~~~~~~  BEGIN PROCESS: " + "(dupesremove2_function) ~~~~~~~~~~~~~~")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    fno = 0
    for filename in sorted(os.listdir(path)):

        if filename.endswith(".txt"):

            fno += 1
            prevcol3 = ""
            d=[]

            with open(filename,'r',encoding="ISO-8859-1") as infile:
                for line in infile.readlines():
                    data = line.strip().split('|')
                    d.append(data)
#            d.sort(key=itemgetter(2))                 #sort the list `d` with the 2 item(3th column) of your sublist.

            with open('outfile.000','w') as outfile:
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
            with open('outfile.000','r',encoding="ISO-8859-1") as infile:
                fno += 1
                for line in infile.readlines():
                    data = line.strip().split('|')
                    d.append(data)
#            d.sort(key=itemgetter(0))

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

            pre, ext = os.path.splitext(filename)
            os.rename("outfile2.txt", "+" + pre[2:] + ".m3u8")

            os.remove("outfile.000")
            os.remove(filename)
            os.remove("+-" + pre[2:] + ".m3u")


    print ("---------------------------")
    print ("Total Files: " + str(fno))
    print ("---------------------------")
    print ("")



if __name__ == "__main__":
    
    dupesmerge_function()     

    dupesremove1_function()

    dupesremove2_function()


                    