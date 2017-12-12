#! /usr/bin/python

data=open("day11_data").read().split(",")
n=w=nmax=wmax=float(0)
for i in data:
	if i == "n":
		n+=1
	elif "nw" in i:
		n+=0.5
		w+=1
	elif "ne" in i:
		n+=0.5
		w-=1
	elif i == "s":
		n-=1
	elif "sw" in i:
		n-=0.5
		w+=1
	elif "se" in i:
		n-=0.5
		w-=1
	if abs(n)>abs(nmax):
		nmax=n
	if abs(w)>abs(wmax):
		wmax=w

## Part 1
if 2*abs(n)<abs(w):
	step = abs(w)
else:
	step = abs(w)/2+abs(n)
print step

## Print 2
if 2*abs(nmax)<abs(wmax):
	stepmax = abs(wmax)
else:
	stepmax = abs(wmax)/2+abs(nmax)
print stepmax
