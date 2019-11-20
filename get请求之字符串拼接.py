import urllib.response
import urllib.request
import urllib.parse
from urllib import response

URL='https://baike.baidu.com/item/'
new_url="相声有新人/22779051"
new_url=urllib.parse.quote(new_url)
date={
    "fr":"aladdin"
}
date=urllib.parse.urlencode(date)
URL=URL+new_url+"?"+date
headers={
    "user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36"
}
request=urllib.request.Request(URL,headers=headers)
response=urllib.request.urlopen(request)
html=response.read().decode()
print(html)