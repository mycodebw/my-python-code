#!/usr/bin/python -w

stock_price = {'google':716, 'apple':105, 'facebook':109, 'microsoft':50, 'baidu':90, '360':75, 'alibaba':88}

while True:
	try:
		money = input('Please input your money: ')
		break
	except:
		print "You input error,Please input again"
stock_list=[]

while True:
	print "\nYou can buy these stock: \n"
	for keys,values in stock_price.items():
		print keys,values
		continue
	if money <= min(stock_price.values()):
		print "\nYou money is %s, You have no enough money buy any stock\n" % money
		if stock_list:
			print "You buyed stock is %s" % str(stock_list)
		exit()
	choose = raw_input('\nYou have %s$,You can buy these stock: \n' % money)
	choose = choose.strip()
	if choose in ('q','quit'):
		print "Thank you for your choose to purchase shares in the stock market"
                exit()
	
	if choose not in stock_price:
		print "The stock is not stock market, please input again"
		continue
	
	price = stock_price[choose]
	if money > price:
		stock_list.append(choose)
		money -= price
		print "You surplus is %s" % money
