# -*- coding: utf-8 -*-
#适用版本python=2.7
import urllib
page = urllib.urlopen("http://www.baidu.com")  #获取网页
dom = page.read()  #得到页面的文本
print(dom)