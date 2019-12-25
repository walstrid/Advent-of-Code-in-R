#! /usr/bin/python

## Part 1
def khash(INPUT):
	lengths=[]
	for char in INPUT:
		lengths+=[ord(char)]
	lengths+=[17, 31, 73, 47, 23]
	pos=skip=0
	rev=[]
	seq=range(0,256)
	
	for j in range(0,64):
		for i in lengths:
			n=0
			rev=[seq[x % len(seq)] for x in range(pos,pos+i)]
			rev.reverse()
			for x in range(pos,pos+i):
				seq[x % len(seq)]=rev[n]
				n+=1
			pos+=i+skip
			skip+=1
	dense=[0]*16
	m=0
	for k in range(0,256,16):
		for j in range(0,16):
			dense[m]^=seq[k:k+16][j]
		m+=1
	KnotHash=""
	for i in dense:
		KnotHash+=str(format(i,'02x'))
	return KnotHash


puzzle="hfdlxzhv"
grid=[]
for i in range(0,128):
	rhash = khash(puzzle+"-"+str(i))
	grid+=[bin(int(rhash,16))[2:]]
print sum(x.count("1") for x in grid)

## Part 2
			
