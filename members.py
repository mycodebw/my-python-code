#!/usr/bin/python -w

#coding:utf-8

import sys

a = open('/root/python_members.txt','r')
content = a.readlines()

while True:
	b=raw_input('Please student search is :')
	print b 
	if b == 'all':
		for lines in content:
			print lines
	elif '-' in b :
		begin, after = b.split('-')
		for lines in content[int(begin)-1:int(after)]:
			print lines
#	elif b :
#		for lines in content[int(b)-1]:
#			print lines
	elif b in ('q','quit'):
		exit()
	elif b not in str(content):
		print "sorry,please input is error"
		
