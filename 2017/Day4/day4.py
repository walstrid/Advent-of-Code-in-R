#! /usr/bin/python

data=open("./day4_data","r")
a = data.readlines()
data.close()

## Part 1
invalid=0
for line in a:
	l={}
	for word in line.split():
		if word in l:
			invalid+=1
			break
		else:
			l[word]=1
print len(a)-invalid

## Part 2
invalid=0
for line in a:
	l=()
	dic={}
	for word in line.split():
		dic={}
		for string in word:
			if string in dic:
				dic[string]+=1
			else:
				dic[string]=1
		if dic in l:
			invalid+=1
			break
		else:
			l=(dic,)+l
print len(a)-invalid
		
