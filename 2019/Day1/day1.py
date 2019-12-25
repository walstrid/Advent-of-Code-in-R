#! /usr/bin/python3

import math
data=open("./input.txt","r")
a=data.readlines()
data.close()

## Part 1
total=0
for line in a:
    fuel=math.floor(float(line)/3.0)-2
    total+=fuel
print total

## Part 2

total=0
for line in a:
    fuel=math.floor(float(line)/3.0)-2
    total+=fuel
    while fuel > 0:
        fuel=math.floor(fuel/3.0)-2
        if fuel > 0:
            total+=fuel
print total
