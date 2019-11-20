import urllib.request
daili_handler=urllib.request.ProxyHandler({"https":"120.83.108.71:9999"})
null_handler=urllib.request.ProxyHandler({})
proxy_switch=False
if proxy_switch:
    opener=urllib.request.build_opener(daili_handler)
else:
    opener=urllib.request.build_opener(null_handler)
request=urllib.request.Request("http://www.baidu.com")
response=opener.open(request)
print(response.read().decode())
