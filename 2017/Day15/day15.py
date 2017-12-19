#! /usr/bin/python

## Part 1
A=618
B=814
judge=0
for i in range(0,40000000):
	A=(A*16807)%2147483647
	B=(B*48271)%2147483647
	lA=len(bin(A))
	lB=len(bin(B))
	if bin(A)[(lA-16):lA] == bin(B)[(lB-16):lB]:
		judge+=1
print judge

## Part 2
A=618
B=814
judge=0
vA=[]
vB=[]
while len(vA) < 5000000 or len(vB) < 5000000:
	A=(A*16807)%2147483647
	B=(B*48271)%2147483647
	if A%4 == 0:
		vA+=[A]
	if B%8 == 0:
		vB+=[B]
for i in range(0,5000000):
	lA=len(bin(vA[i]))
	lB=len(bin(vB[i]))
	if bin(vA[i])[lA-16:lA] == bin(vB[i])[lB-16:lB]:
		judge+=1
print judge
