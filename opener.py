import urllib.request
http_hander=urllib.request.HTTPHandler()
opener=urllib.request.build_opener(http_hander)
http_proxy=urllib.request.ProxyHandler({"https":"120.83.108.71:9999"})#构建一个代理对象
opener=urllib.request.build_opener(http_proxy)#使用代理
request=urllib.request.Request("http://www.baidu.com")
response=opener.open(request)
print(response.read().decode())
"""
感觉没太大重要的东西
"""