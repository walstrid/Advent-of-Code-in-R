#! /usr/bin/python

##Part 1
a=open("day7_data").read().split("\n")
nodes={}
roots=[]
branches=[]
val={}
for line in a[0:len(a)-1]:
	ls=line.split()
	vars()[ls[0]]=int(ls[1][1:len(ls[1])-1])
	val[ls[0]]=vars()[ls[0]]
	if "->" in line:
		node=line.split(" -> ")
		nodes[node[0].split()[0]]=node[1].split(", ")
		roots=roots+[node[0].split()[0]]
		branches=branches+node[1].split(", ")
for i in roots:
	if i not in branches:
		root=i
print root

## Part 2
level={0:[root]}
for i in range(1,6):
	for element in level[i-1]:
		try:
			if i in level.keys():
				level[i]=level[i]+nodes[element]
			else:
				level[i]=nodes[element]
		except KeyError:
			None
rev=level.keys()
rev.reverse()
for i in rev:
	for element in level[i]:
		try:
			for branch in nodes[element]:
				val[element]+=val[branch]
		except KeyError:
			None
c=i=0
while c!="n":
	n=0
	for element in nodes[level[i][c]]:
		print "["+str(n)+"] "+str(val[element])+" "+element
		n+=1
	i+=1
	print "### Select index or enter 'n' to exit"
	c=input()
print "### Enter outlier's strings"
outlier=input()
print "### Enter difference of weight"
diff=input()
print "%d %d = %d" %(outlier,-diff,outlier-diff)
