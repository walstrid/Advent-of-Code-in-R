#! /usr/bin/python

data=open("./day5_data","r")
a=data.readlines()
data.close()

## Part 1
nice=0
for line in a:
	vowels=0
	forbidden=0
	double=0
	line=line+"0"
	for i in range(0,len(line)-1):
		if line[i] in ("a","e","i","o","u"):
			vowels+=1
		if line[i:i+2] in ("ab","cd","pq","xy"):
			forbidden+=1
		if line[i] == line[i+1]:
			double+=1
	if vowels>2 and forbidden==0 and double>0:
		nice+=1
print nice

## Part 2
nice=0
for line in a:
	double=0
	pair=0
	line=line+"00"
	l={}
	for i in range(0,len(line)-2):
		if line[i] == line[i+2]:
			double+=1
		if line[i:i+2] in l:
			l[line[i:i+2]]+=1-i
		else:
			l[line[i:i+2]]=i
	for j in l:
		if l[j]<0:
			pair+=1
	if double>0 and pair>0:
		nice+=1
print nice
