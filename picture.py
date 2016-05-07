#!/usr/bin/python -w

#coding:utf8

import re
import urllib

def get_html(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html

def get_image(html):
	reg = r'src="(.+?\.jpg)" pic_ext'
	imgre = re.compile(reg)
	image_list = imgre.findall(html)

	for image,index in enumerate(image_list):
		urllib.urlretrieve(imgurl,'%s.jpg' % index)

if __name__ == '__main__':
	html = get_html("http://tieba.baidu.com/p/2460150866")
	print html 
	#get_image(html)	
