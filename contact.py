#!/usr/bin/python -w

import os 
import pickle

def main():
	if not os.path.exists(r'/root/contact.data'):
		f = open('/root/contact.data','wb')
		temp = {'total':0}
		pickle.dump(temp,f)
		f.close()
	point()
	while True:
		_input = raw_input('Please input your choose:')
		if _input == '*':
			point()
			continue
		elif _input == '1':
			showall()
			continue
		elif _input == '2':
			add()
			continue
		elif _input == '3':
			name = raw_input('Please enter the delete of the contact: ')
			delete(name)
			continue
		elif _input == '4':
			name = raw_input('Please enter the find of the contact: ')
			find(name)
			continue
		elif _input == '5':
			change()
			continue
		elif _input == '6':
			quit()
		else:
			print "input isn't exists,Please input again"	

def point():
	print "Show Toolkip: *"
	print "Show all contact: 1"
	print "Add contact: 2"
	print "Delete contact: 3"
	print "Find contact: 4"
	print "Change contact: 5"
	print "Quit contact: 6"

def showall():
	f = open('/root/contact.data','rb')
	info = pickle.load(f)
	#print info
	print "How many contact is %s" % info['total']
	for key in info:
		if key != 'total':
			print "%s : %s" % (key , info[key])
	f.close()	

def add():
	f = open('/root/contact.data','rb')
	info = pickle.load(f)
	f.close()
	name = raw_input('Please input contact name :')
	if name in info:
		print "contact is exists,Please input again"
	else:
		number = input('Please input celephone number: ')
		info['total'] += 1
		info.setdefault(name,number)
		f = open('/root/contact.data','wb')
		pickle.dump(info,f)
		f.close()
		print "Add is OK"

def delete(name):
	f = open('/root/contact.data','rb')
	info = pickle.load(f)
	f.close()
	if name in info:
		info.pop(name)
		info['total'] -= 1
		f = open('/root/contact.data','wb')
		pickle.dump(info,f)
		print "Delete is OK"
	else:
		print "Delete contact isn't exists"

def change():
	f = open('/root/contact.data','rb')
	info = pickle.load(f)
	f.close()
	name = raw_input('Please enter the change of the contact: ')
	#print name
	if name in info:
		number = input('Please input your celephone number: ')
		info[name] = number
		#print info
		f = open('/root/contact.data','wb')
		pickle.dump(info,f)
		print "Change is OK"
	else:
		print "Contact isn't exists"
		
		

def find(name):
	f = open('/root/contact.data','rb')
	info = pickle.load(f)
	f.close()
	if name in info:
		print "%s celephone is %s" % (name, info[name])
	else:
		print "Contact is exists"	
	

def quit():
	exit()

if __name__ == '__main__':
	main()
