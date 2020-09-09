import urllib.request
import urllib.parse
# parse a url and read data form it
# x=urllib.request.urlopen("https://www.google.com")
# print(x.read())
url="https://pythonprogramming.net/"
Value={'s':'basic','submit':'search'}
data=urllib.parse.urlencode(Value)
parseData=data.encode('utf-8')
request=urllib.request.Request(url,parseData)
x=urllib.request.urlopen(request)
# print(x.read())

try :
    url = "https://pythonprogramming.net/"
    Value = {'s': 'basic', 'submit': 'search'}
    data = urllib.parse.urlencode(Value)
    parseData = data.encode('utf-8')
    request = urllib.request.Request(url, parseData)
    x = urllib.request.urlopen(request)
    readUrl=x.read()
    saveFile=open("readUrlFile.txt",'w')
    saveFile.write(str(readUrl))
    saveFile.close()
except Exception as e:
    print(str(e))