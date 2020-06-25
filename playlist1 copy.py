path = '/users/henryvalevich/list.m3u'
f = open(path,'r')
searchlines = f.readlines()
f.close()

for i, line in enumerate(searchlines):
    if "#EXTINF:" in line: 
        for l in searchlines[i:i+3]: print l,
        print