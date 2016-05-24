#!/usr/bin/python -w

import sys
import time

class Lion:
	
	def __init__(self, name,age,weight,gender):
		self.name = name
		self.age = age
		self.weight = weight
		self.gender = gender

class Nana(Lion):
	
	def __init__(self, face_score, voice):
		self.face_score = face_score
		self.voice = voice

class Sindy(Lion):
	
	def __init__(self, face_score, voice):
		self.face_score = face_score
		self.voice = voice

def fight():
	simba = Lion('Simaba',4,60,'male')
	scar = Lion('Scar',11,110,'male')
	year = 0
	times = 0
	
	while simba.weight < scar.weight:
		simba.weight -= 4
		times += 1
		year += 1
		simba.weight += 15
		simba.age += 1
		time.sleep(1)
	print simba.age, simba.weight, year

def choose_wife():
	nana = Nana(77, 87)
	sindy = Sindy(75, 89)

	nana_ret = nana.face_score + nana.voice
	sindy_ret = sindy.face_score + sindy.voice

if __name__ == '__main__':
	fight()
	choose_wife()
