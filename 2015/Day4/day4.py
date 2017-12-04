#! /usr/bin/python

## Part 1
import md5
code="bgvyzdsv"
res=""
n=0
while res[0:5] != "00000":
	n+=1
	res=md5.new(code+str(n)).hexdigest()
print n

## Part 2
res=""
n=0
while res[0:6] != "000000":
        n+=1
        res=md5.new(code+str(n)).hexdigest()
print n
