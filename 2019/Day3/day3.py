#! /usr/bin/python3

data=open("./input.txt","r")
a=data.readlines()
data.close()

## Part 1

def logcoord(line):
    coord=line.split(",")
    x=y=0
    wire=[]
    for mouv in coord:
        n=int(mouv[1:])
        for i in range(0,n):
            if "R" in mouv:
                x+=1
            if "L" in mouv:
                x-=1
            if "U" in mouv:
                y+=1
            if "D" in mouv:
                y-=1
            wire.append((x,y))
    return wire

wire1=logcoord(a[0])
wire2=logcoord(a[1])


identicals=list(set.intersection(*map(set,[wire1,wire2])))
manh_dist=[]
for coord in identicals:
    manh_dist.append(sum(map(abs,coord)))
print min(manh_dist)


## Part 2
allsum=[]
for elem in identicals:
    allsum.append(wire1.index(elem)+wire2.index(elem))
print min(allsum)+2


