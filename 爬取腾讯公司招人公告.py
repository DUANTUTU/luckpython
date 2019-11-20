import json
import jsonpath
import urllib.request
import re
from bs4 import BeautifulSoup
from lxml import etree
class Spider(object):
    def __init__(self):
        self.begin_page=int(input("请输入起始页"))
        self.end_page=int(input("请输入结束页"))
        self.baseurl="http://hr.tencent.com/"
    def load_page(self):
        """"
        这里留个彩蛋
        SUNSHUOwoshinidie
        """
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
        headers={"User-Agment":user_agent}
        for page in range(self.begin_page,self.end_page):
            url=self.baseurl+"search.html?index="+str(page)
            request=urllib.request.Request(url,headers=headers)
            response=urllib.request.urlopen(request)
            html=response.read().decode("utf-8")
            #print(html)
            return html
    # def parse_page(self,html):
        # name_list=re.findall(r'lid=0">(.*?)</a>',html)
        # links_list=re.findall(r'<a target="_blank" href="(.*?)">',html)
        # temp_list=re.findall(r'<td>(.*?)</td>',html)
        # others_list=temp_list[4:]
        # category_list=others_list[0::4]
        # counts_list=others_list[1::4]
        # location_list=others_list[2::4]
        # publist_time_list=others_list[3::4]
        # items = []
        # for i in range(0, len(name_list)):
        #     item = {}
        #     item["职位名称"] = name_list[i]
        #     item["详细链接"] = self.base_url + links_list[i]
        #     item["职位类别"] = category_list[i]
        #     item["招聘人数"] = counts_list[i]
        #     item["工作地点"] = location_list[i]
        #     item["发布时间"] = publist_time_list[i]
        #     items.append(item)
        # print(items)
    def parse_page(self,html):
        root=etree.HTML(html)
        links=root.xpath("//td[@class='1 square']/a/@href")
        names=root.xpath("//td[@class='1 square']/a/@text()")
        categorys=root.xpath("td[@class='even']/td[2]|//tr[@class='odd']/td[2]")
        counts=root.xpath("td[@class='even']/td[3]|//tr[@class='odd']/td[3]")
        locations=root.xpath("td[@class='even']/td[4]|//tr[@class='odd']/td[4]")
        publish_times=root.xpath("td[@class='even']/td[5]|//tr[@class='odd']/td[5]")
        items = []
        for i in range(0, len(names)):
            item = {}
            item["职位名称"] = names[i]
            item["详细链接"] = self.base_url + links[i]
            item["职位类别"] = categorys[i].text
            item["招聘人数"] = counts[i].text
            item["工作地点"] = locations[i].text
            item["发布时间"] = publish_times[i].text
            items.append(item)
        print(items)

        """
        html=BeautifulSoup(html,"lxml")
        result=html.select('tr[class="even"]')
        result2=html.select('tr[class="odd"]')
        result+=result2
        """
        #self.save_file(items)
    def save_file(self,items):
        file=open('tencents.txt',"wb+")
        file.write(str(items).encode())
        file.close()
if __name__ == '__main__':
    spider = Spider()
    return_html=spider.load_page()
    spider.parse_page(return_html)