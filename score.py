#!/usr/bin/python -w
#coding=utf-8
score = input('please score is: ')

while score > 0 :
	if score >= 60 and score < 70:
		print "score  is pass"
		break
	elif score >= 70 and score <= 85:
		print "score is good"
		break
	elif score >= 85 and score <= 100: 
		print "score is excellent"
		break
	elif score <= 60:
		print "score is failed"
		break 
