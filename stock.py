#!/usr/bin/python -w

#coding:utf-8

import sys

stock_price = {'google':716, 'apple':105, 'facebook':109, 'microsoft':50, 'baidu':90, '360':75, 'alibaba':88}

while True:
	try:
		money=input('Please input your money: ')
		break
	except:
		print "your input is not correct, please input a number"
stock_list=[]
	
while True:
	print "\nCan you buy the stock at present:"
	for index,price in stock_price.items():
		print '%s......%s' % (index,price)

	if money < min(stock_price.values()):
		print "\nsorry, you have no enough money to buy any stock\n"
		if stock_list:
			print "\n you have this stock:\n %s" % str(stock_list)
		exit()
	
	_choose = raw_input('You have %s$, Please choose these stock: ' % money)
	
	_choose = _choose.strip()
	
	if _choose not in stock_price:
		print "\nYou choose stock inexistence, Please choose stock again\n"
		continue
		
	price = stock_price[_choose]
	if money >= price:
		stock_list.append(_choose)
		money -= price
		print "\n You balance is %s \n" % money
	else:
		print "You can't buy any stock"
