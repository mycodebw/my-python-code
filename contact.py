#!/usr/bin/python -w

#coding=utf8

import pickle,os

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
		temp={'temp' : 0}
		pickle.dump(temp, f)
		f.close()

	point()
	while True:
		_input = input("Pease input your choose: ")
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
