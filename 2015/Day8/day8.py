#! /usr/bin/python

data=open("day8_data").read().split("\n")
data.pop()

## Part 1
str_nb=0
char_nb=0
escape=False
skip=0
for line in data:
	for char in line:
		if char != " ":
			str_nb+=1
			if skip>0:
				skip-=1
			elif char == "\"" and escape==False:
				pass
			elif char == "\\" and escape==False:
				escape=True
				char_nb+=1
			elif escape==True and (char == "\"" or char =="\\"):
				escape=False	
			elif escape==True and char=="x":
				escape=False
				skip=2
			else:
				char_nb+=1
print str_nb - char_nb

## Part 2
str_nb=0
encode_nb=0
for line in data:
	encode_nb+=2
	for char in line:
		str_nb+=1
		if char == "\"" or char == "\\":
			encode_nb+=2
		else:
			encode_nb+=1
print encode_nb - str_nb
