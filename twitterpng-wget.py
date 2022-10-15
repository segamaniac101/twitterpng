import wget

url = input('Enter the Twitter image URL: ')
png = '?format=png&name=4096x4096'
sum = url + png

print (sum)

filename = wget.download(sum)

print (filename, 'was successfully downloaded.')
