#! /usr/bin/python

data = open("day13_data").read().split("\n")
data.pop()
fw={}
for line in data:
	line=line.split(": ")
	fw[int(line[0])]=int(line[1])

## Part 1
n=0
sev=0
while n < fw.keys()[len(fw)-1]+1:
	if n in fw:
		if n%(2*(fw[n]-1)) == 0:
			sev+=fw[n]*n
	n+=1
print sev

## Part 2
delay=0
caught=True
while caught:
	caught=False
	for i in fw.keys():
		if (i+1+delay) % (2*(fw[i]-1)) == 0:
			caught=True
			break
	delay+=1
print delay
