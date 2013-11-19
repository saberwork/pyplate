import urllib

url='http://ip.jsontest.com/?callback=showMyIP'

u = urllib.urlopen(url)
# u is a file-like object
print u.read()