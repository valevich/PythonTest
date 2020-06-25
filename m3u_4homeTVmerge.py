import os
from shutil import copyfile

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


print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("~~~~~~~~~~~~~~  BEGIN PROCESS: " + "(merge4HomeTV_function) ~~~~~~~~~~~~~~")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


playlistpath = "/Users/henryvalevich/odrive/DOWNLOADS_Box_25G_valevich@aol.com/Downloads/IPTV/Playlists/4hometv10/"
sourcepath = "/Users/henryvalevich/odrive/DOWNLOADS_Box_25G_valevich@aol.com/Downloads/IPTV/Playlists/4hometv10/Edem Source/"
backuppath = "/Users/henryvalevich/odrive/DOWNLOADS_Box_25G_valevich@aol.com/Downloads/IPTV/Playlists/4hometv10/Backup/"

#concat2 = open("output.m3u").read()

files = os.listdir(path)
if '.DS_Store' in files:
    files.remove('.DS_Store')
if 'Dead' in files:
    files.remove('Dead')
if 'Backup' in files:
    files.remove('Backup')
for idx, infile in enumerate(files):
    print ("File #" + str(idx + 1) + "  " + infile)
concat = ''.join([open(path + f,encoding="ISO-8859-1").read() for f in files])


for filename in sorted(os.listdir(sourcepath)):

    if filename.endswith(".m3u") or filename.endswith(".m3u8"):

        print ("Creating File: " + filename)
        with open(sourcepath + filename, 'r',encoding="ISO-8859-1") as searchfile:

            concat2 = open(sourcepath + filename).read()
            with open(playlistpath + filename, "w") as fo:
                fo.write(concat2 + concat)

            str_idx = int(filename.find("."))
            newname = (date_time + "_" + filename[:str_idx] + ".m3u")
            copyfile(playlistpath + filename, backuppath + newname)

                

print ("")

 #if prevno > 1:
 #    os.rename("output.txt", ("+" + prevfile + ".m3u"))
 #else:    
 #    os.rename("output.txt", ("-" + prevfile + ".m3u"))
 #
 #print ("---------------------------------------------------")
 #print ("Total Files: " + str(fno))
 #print ("---------------------------------------------------")
    
                