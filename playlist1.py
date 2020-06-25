import os
infile = '/users/henryvalevich/list.m3u'
tempfile = open("output.txt","w")

with open(infile, 'r') as searchfile:

    for line in searchfile:
    	print line
    	tempfile.writelines(line)
    	
        if 'http://' in line:
            filename = line.replace("http://","")
            filename = filename.replace("/","_")


tempfile.close()
searchfile.close

old_file = os.path.join("/users/henryvalevich/", "output.txt")
new_file = os.path.join("/users/henryvalevich/", filename + ".m3u")
os.rename(old_file, new_file)