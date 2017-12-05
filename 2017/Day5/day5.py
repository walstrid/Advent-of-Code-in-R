#! /usr/bin/python

## Part 1
data=open("./day5_data","r")
a=data.readlines()
data.close()
a=map(int,a)+[0]
pos=0
n=0
while pos < len(a)-1:
	a[pos]+=1
	pos+=a[pos]-1
	n+=1
print n

## Part 2
data=open("./day5_data","r")
a=data.readlines()
data.close()
a=map(int,a)+[0]
pos=0
n=0
while pos < len(a)-1:
	if a[pos]<3:
		a[pos]+=1
		pos+=a[pos]-1
	else:
		a[pos]-=1
		pos+=a[pos]+1
	n+=1
print n
