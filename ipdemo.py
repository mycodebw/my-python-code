#!/usr/bin/python -w

from IPy import IP 

ip = IP('192.168.10.0/24')

print ip.len()

for i in ip:
	print (i)
