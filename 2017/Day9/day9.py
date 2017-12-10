#! /usr/bin/python

data=open("day9_data").read()
garbage=score=i=nest=shit=0
while i < len(data):
	if data[i] == "!" and garbage==1:
		i+=2
	else:
		if data[i] == "<" and garbage==0:
			garbage=1
		elif data[i] == ">" and garbage==1:
			garbage=0
		elif garbage==1:
			shit+=1
		elif data[i] == "{" and garbage==0:
			nest+=1
			score+=nest
		elif data[i] == "}" and garbage==0 and nest>0:
			nest-=1
		i+=1
## Part 1
print score
## Part 2
print shit
