import glob   
import os

path = '/Users/henryvalevich/Downloads/M3U-in/*.m3u'   
files=glob.glob(path)   

for file in files: 
    print file
    tempfile = open("output.txt","w")
    
    with open(file, 'r') as searchfile:
    	for line in searchfile:
    		print line
    		tempfile.writelines(line)
    	
        	if 'http://' in line:
        		filename = line.replace("http://","")
        		filename = filename.replace("/","_")

	tempfile.close()
	searchfile.close

	old_file = os.path.join("/users/henryvalevich/", "output.txt")
	new_file = os.path.join("/Users/henryvalevich/Downloads/M3U-out/", filename + ".m3u")
	os.rename(old_file, new_file)