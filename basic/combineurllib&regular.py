import urllib.request
import urllib.parse
import re
url='https://www.pythonprogramming.net'
value={'s':'basic','submit':'search'}
data=urllib.parse.urlencode(value)
dataEncode=data.encode('utf-8')
request=urllib.request.Request(url,dataEncode)
openReq=urllib.request.urlopen(request)
readReq=openReq.read()

paragragh=re.findall(r'<p>(.*?)</p>',str(readReq))
for eachparagragh in paragragh:
    print(eachparagragh)