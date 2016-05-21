#!/usr/bin/python -w

#coding=utf8

import pickle
import os

def showall():
	f=open('/root/contact.data','r')
	info = pickle.load(f)
	print ("How many contacts : %s" % info['total'])
	#print ("How many contacts : %s" % info)
	for key in info:
		if key != 'total':
			print("%s : %s" %(key, info[key]))
	f.close()
	
def search():
	f=open('/root/contact.data','rb')
	info = pickle.load(f)
	f.close()
	if name in info:
		print ("%s cellphone number is: %s" % (name, info[name]))
	else:
		print ("The contact does not exist")

def add():
	f=open('/root/contact.data','rb')
        info = pickle.load(f)
        f.close()
	name = raw_input("Please enter the add contact name: ")
	if name in info:
		print ("Contact already exists,do not need to add")
	else:
		number = input("Please input your cellphone number: ")
		#info['total'] +=1
		info.setdefault(name, number)
		f=open('/root/contact.data','wb')
		pickle.dump(info, f)
		f.close()
		print ("Add is OK")
def change():
	f=open('/root/contact.data','rb')
        info = pickle.load(f)
        f.close()
	if len(info) == 1:
		print "Contact is zero"
		return
	name = raw_input("Please enter the modify contact name: ")
	if name in info:
		number = input("Please input your cellphone number of the modified: ")
		info[name] = number
		f=open('/root/contact.data','wb')
                pickle.dump(info, f)
                f.close()
		print ("Modify is OK")

def delete():
	f=open('/root/contact.data','rb')
        info = pickle.load(f)
        f.close()
	if name in info:
		info.pop(name)
		info['total'] -= 1
		f=open('/root/contact.data','rb')
		pickle.dump(info, f)
		f.close()
		print ("Delete is OK")
	else:
		print ("The contact does not exist,cannot be deleted! ")

def exit():
        exec("quit()")


def point():
	print("*************************")
	print("Show Tooltip:*")
	print("Display all contact:0")
	print("Add contact:1")
	print("Find contact:2")
	print("Delete contact:3")
	print("Modify contact information:4")
	print("Quit contact:5")
	print("*************************")

def main():
	if not os.path.exists(r'/root/contact.data'):
		f = open('/root/contact.data','wb')
		temp={'total' : 0}
		pickle.dump(temp, f)
		f.close()

	point()
	while True:
		_input = raw_input("Pease input your choose: ")
		if _input == '*':
			point()
		elif _input == '0':
			showall()
			continue
		elif _input == '1':
			add()
			continue
		elif _input == '5':
			exit()
			continue
		elif _input == '2':
			name = raw_input("Please enter the to find the name of the contact: ")
			search(name)
			continue
		elif _input == '3':
			name = raw_input("Please enter the want to delete the name of the contact: ")
			delete(name)
			continue
		elif _input == '4':
			change()
			continue
		else:
			print("Input option does not exist,please enter again! ")
			continue

if __name__ == '__main__':
	main()
