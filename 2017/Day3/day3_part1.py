#! /usr/bin/python

## Part 1
import math
a=347991
d=int(math.sqrt(a))+1 # length of one size
dsq=d**2
da=dsq-a
r=da%d # rest = diff from border
q=int(da/d)
l=[1,2]
if d%2==0:
	md=abs(d-d/2) + abs(r+1-d/2)
else:
	md=abs(1-int(d/2+1)) + abs(r+l[q]-int(d/2+1))
print(md)



