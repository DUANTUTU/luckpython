import requests
import urllib.request
import urllib.parse
#https://tieba.baidu.com/f?kw=%C0%EE%D2%E3&pn=250
def tieba_spider(url,begin_page,end_page):
    kw = input("请输入要爬取的贴吧名字：")
    begin_page = int(input("请输入起始页面："))
    end_page = int(input("请输入结束的页面："))
    url = "https://tieba.baidu.com/f?"
    key = urllib.parse.urlencode({"kw": kw})
    url = url + key
    tieba_spider(url,begin_page,end_page)
def load_page(url,filename):
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36"}
    request=urllib.request.Request(url,headers=headers)
    return urllib.request.urlopen(request).read()
def write_page(html,filename):
    print("正在保存"+filename)
    with open(filename,"w",encoding="UTF-8") as file:
        file.write(html.decode("UTF-8"))
kw = input("请输入要爬取的贴吧名字：")
begin_page = int(input("请输入起始页面："))
end_page = int(input("请输入结束的页面："))
url = "https://tieba.baidu.com/f?"
key = urllib.parse.urlencode({"kw": kw})
url = url + key
for page in range(begin_page,end_page+1):
    pn=(page-1)*50
    file_name="第"+str(page)+"页.html"
    full_url=url+"&pn="+str(pn)
    html=load_page(full_url,file_name)
    write_page(html,file_name)



