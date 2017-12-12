#! /usr/bin/python

data = open("day12_data").read().split("\n")
data.pop()

## Part 1
val={}
for line in data:
	line=line.split(" <-> ")
	val[line[0]]=line[1].split(", ")
count=["0"]
for element in count:
	for i in val[element]:
		if i not in count:
			count+=[i]
print len(count)

## Part 2
total = count
group=1
for value in val.keys():
	if value not in total:
		count=[value]
		total+=[value]
		group+=1
		for element in count:
			for i in val[element]:
				if i not in count:
					count+=[i]
					total+=[i]
print group
