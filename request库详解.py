import urllib
import urllib.request
import urllib.parse
url="http://www.baidu.com"
pet={
    "data":"我有一只ad驴"
}
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}
pet=bytes(urllib.parse.urlencode(pet).encode())
request=urllib.request.Request(url=url,data=pet,headers=headers)
response=urllib.request.urlopen(request)
#print(response.read().decode())
"""
构造对象访问，其实一般的网页不构造也能够进行爬取，构造对象之后请求会变成post请求
1.data数据必须进行编码和byte之后才能够发送
2.urlencode的参数是词典，它可以将key-value这样的键值对转换成我们想要的格式
3.encode 是字符编码可以将字符编码进行转换比如 UTF-8
4.quote 可以将单个字符进行转换，unquote 可以将已经转换的字符进行解码
"""
print(pet)
print(urllib.parse.unquote(str(pet)))