#!/usr/bin/python -w
#coding=utf-8

while True :
	score = input('please score is: ')
	if score >= 60 and score < 70:
		print "score  is pass"
		continue
	elif score >= 70 and score < 85:
		print "score is good"
		continue
	elif score >= 85 and score < 100: 
		print "score is excellent"
		continue
	elif score < 60:
		print "score is failed"
		continue 
