import os
import re
from datetime import datetime
os.system('clear')


#path = str(input("Enter Path: [default:/Users/henryvalevich/Downloads/Temp Sports] \n")).lower().strip()
#if len(path) == 0 :
#    path = "/Users/henryvalevich/Downloads/Temp Sports/"
#
#if os.path.exists(path):
#    print('Valid Path: ' + path) 
#else:
#    print('Path Does Not Exist!')
#    sys.exit()
path = "/Users/henryvalevich/Downloads/Temp Sports/"


print ("=====================  START  =====================")
now = datetime.now() # current date and time
date_time = now.strftime("%m%d%Y")
#path = "/users/henryvalevich/Downloads/Temp/"
retval = os.getcwd()
print ("Current working directory %s" % retval)
os.chdir( path )
retval = os.getcwd()
print ("Directory changed successfully %s" % retval)



#==========================================  MERGEFOLDERS FUNCTION  ==========================================
def mergeFolders_function():

    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("~~~~~~~~~~~~~~  BEGIN PROCESS: " + "(mergeFolders_function) ~~~~~~~~~~~~~~")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    path1 = "/Users/henryvalevich/Downloads/Temp/"
    path2 = "/Users/henryvalevich/Downloads/Temp Sports/"

    for filename in sorted(os.listdir(path1)):

        if filename.endswith(".m3u") or filename.endswith(".m3u8"):

            if (os.path.isfile(path2 + filename)):
                print("Error: %s file already exists" % filename)
                continue
                
            print ("Copying File: " + filename)
            os.replace(path1 + filename, path2 + filename)


    print ("")



#==========================================  DUPESMERGE FUNCTION  ==========================================
def rename_function():

    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("~~~~~~~~~~~~~~  BEGIN PROCESS: " + "(rename_function) ~~~~~~~~~~~~~~")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


    fno = 0

    for filename in sorted(os.listdir(path)):
    
        if filename.endswith(".m3u") or filename.endswith(".m3u8"):
        
            fsize=os.stat(path + filename)
            if fsize.st_size > 1000000:        #check if the file size is less than 1 MB
                print('FILE SKIPPED - SIZE TOO LARGE:' + fsize.st_size.__str__() + " Filename: " + filename)
                os.rename(filename, ("-SKIPPED-" + filename + ".000"))                
                continue
                
            fno += 1
            renam = "no"
            print ("------------------------------------------------")
            with open(filename, 'r') as searchfile:

                lineno = 0
                pre, ext = os.path.splitext(filename)
    #            print ("Pre: " + pre)
    #            print ("Ext: " + ext)
            
                for line in searchfile:
 
                    line = ''.join([s for s in line if ord(s) < 127])
                
                    if lineno == 3:
                        break
                                
                    if 'http://' in line:
                        lineno += 1
                        oldname = line.replace("http://","")
                        oldname = oldname.replace(":","-")
                        str_idx = int(oldname.find("/"))
                        newname = (oldname[:str_idx] + "_" + str(fno) + "_" + date_time + ext)

                print ("Old Name: " + filename)
                print ("New Name: " + newname)
                os.rename(filename, newname)
                searchfile.close

    print ("---------------------------------------------------")
    print ("Total Files: " + str(fno))
    print ("---------------------------------------------------")




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

                        line = ''.join([s for s in line if ord(s) < 127])
                        
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
                    print ("file = " + filename)
                 

                pre, ext = os.path.splitext(filename)
                os.rename("tempsort.txt", pre + ".txt")
                os.remove(filename)
                

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
            d.sort(key=itemgetter(2))                 #sort the list `d` with the 2 item(3th column) of your sublist.

            with open('outfile.000','w') as outfile:
                for line in d:
                    xline = ('|'.join(line)+'\n')
                    str_idx1 = int(xline.find("|"))
                    str_idx2 = int(xline.find("http://"))
                    col1 = (xline[:str_idx1])
                    col2 = (xline[str_idx1+1:str_idx2-1])
                    col3 = (xline[str_idx2:])
                    if col3 != prevcol3:
                        if "http://blank" not in col3:
                            outfile.writelines(col1 + '|' + col2 + '|' + col3)
                    prevcol3 = col3        

            d=[]
            with open('outfile.000','r',encoding="ISO-8859-1") as infile:
                fno += 1
                for line in infile.readlines():
                    data = line.strip().split('|')
                    d.append(data)
#            d.sort(key=itemgetter(0))                 #sort the list `d` with the 2 item(3th column) of your sublist.

            with open('outfile2.txt','w') as outfile:
                prevcol3 = ""
                lineno = 0
                for line in d:
                    lineno += 1
                    xline = ('|'.join(line)+'\n')
                    str_idx1 = int(xline.find("|"))
                    str_idx2 = int(xline.find("http://"))
                    col1 = (xline[:str_idx1])
                    col2 = (xline[str_idx1+1:str_idx2-1])
                    col3 = (xline[str_idx2:])
                    
                    col3short = (col3.rsplit('/', 1)[0])
                    if prevcol3 != col3short:
                        prevcol3 = col3short
                        outfile.writelines(""+'\n')
                        outfile.writelines("#EXTINF:0,********(" + col3[7:13] + ")********"+'\n')
                        outfile.writelines("#EXTGRP:FOOTBALL"+'\n')
                        outfile.writelines("http://blank"+'\n')
                    outfile.writelines(col1+'\n')
                    if not col2:
                        outfile.writelines("#EXTGRP:FOOTBALL"+'\n')
                    else:
                        outfile.writelines(col2+'\n')
                    outfile.writelines(col3)
                    

            pre, ext = os.path.splitext(filename)
            os.rename("outfile2.txt", pre[2:] + ".m3u")

            os.remove("outfile.000")
            os.remove(filename)


    print ("---------------------------")
    print ("Total Files: " + str(fno))
    print ("---------------------------")
    print ("")




if __name__ == "__main__":

    mergeFolders_function()
    
    rename_function()
    
    dupesmerge_function()     

    dupesremove1_function()

    dupesremove2_function()


                    