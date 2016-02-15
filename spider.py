#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'爬虫'

__author__ = 'Hao Chuan'

import urllib.request as request
import urllib.parse as parse
import string

def baidu_tieba(url,begin_page,end_page):
	for i in range(begin_page,end_page + 1):
		sName = 'e:/test/'+str(i).zfill(5)+'.html'
		print('正在下载第'+str(1)+'个页面，并保存为'+sName)
		m = request.urlopen(url+str(i)).read()
		with open(sName,'wb') as file:
			file.write(m)
		file.close()
if __name__ == "__main__":
	url = "http://tieba.baidu.com/p/"
	begin_page = 1
	end_page = 3
	baidu_tieba(url,begin_page,end_page)