#! /bin/python

# Part One
data = open("input.txt").read().split("\n")
data.pop()
res = 0
for l in data:
	res += int(l)
print res

# Part Two
res = 0
for n in range(1,300):
	print n
	for l in data:
		res+=int(l)
	
