#!/usr/bin/python -w

#a = [1,2,5,9,'sj']
a = [1,2,5,9]
i = 1

for item in a:
	if i %2 ==0 and isinstance(item,int):
		item += 1
		print item	
	elif isinstance(item,str):
		print "list is error"
	i += 1

b=[x for x in range(0,10) if x %2 ==0]
print b 
