#! /usr/bin/python

data=open("./day8_data").read().split("\n")
data.pop()
val={}
allval=[]
for line in data:
	line = line.split(" if ")
	for i in [0,1]:
		if line[i].split()[0] not in val:
			val[line[i].split()[0]]=0
	if eval(str(val[line[1][0:line[1].find(" ")]])+line[1][line[1].find(" "):len(line[1])]):
		if "inc" in line[0]:
			val[line[0].split()[0]]+=int(line[0].split()[2])
		else:
			val[line[0].split()[0]]-=int(line[0].split()[2])
		allval+=[val[line[0].split()[0]]]
## Part 1
print max(val.values())
## Part 2
print max(allval)
