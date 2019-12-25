#! /usr/bin/python

import string
data = open("day16_data").read().split(",")
seq=string.ascii_lowercase[:16]
for i in data:
	if i[0] == "s":
		n=int(i[1:])
		seq=seq[(16-n):16]+seq[0:(16-n)]
	if i[0] == "x":
		
