import urllib.request

opener=urllib.request.build_opener()
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

url = input('Enter the Twitter image URL: ')
png = '?format=png&name=4096x4096'
sum = url + png

print (sum)

filename = urllib.request.urlretrieve(sum)

print (filename, 'was successfully downloaded.')
