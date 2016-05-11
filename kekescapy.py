#encoding=utf-8
import requests
from bs4 import BeautifulSoup
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
kekeurl = "http://www.kekenet.com/cet6/ljtl/"
kekeurl = "http://www.kekenet.com/cet6/ljtl/List_81.shtml"
kekeurl = "http://www.kekenet.com/cet6/ljtl/List_80.shtml"
kekeurl = "http://www.kekenet.com/cet6/ljtl/List_79.shtml"
kekeurl = "http://www.kekenet.com/cet6/ljtl/List_78.shtml"
kekeurl = "http://www.kekenet.com/cet6/ljtl/List_2.shtml"

page = "81"
while(page > 70):
    page = str(page)
    kekeurl = "http://www.kekenet.com/cet6/ljtl/List_"+ page +".shtml"

    r = requests.get(kekeurl)
    r.encoding = "utf-8"
    html = r.text

    soup = BeautifulSoup(unicode(html),"lxml")

    list_soup = soup.find_all("a",href=re.compile("http://www.kekenet.com/.+/.+/.+.shtml"))
    if list_soup.__len__() != 15:
        print "######################################################################page=",page
    with open('kekeyinyu.md', 'a') as f:
        f.write("page="+page+"\n")
        for i in list_soup:
        # print i
        # print "["+i['title']+"]"+"("+i['href']+")"
            line = "["+i['title']+"]"+"("+i['href']+")"+"\n"
            f.write(line)
    page = int(page)
    page -= 1
    # print "page=",page


