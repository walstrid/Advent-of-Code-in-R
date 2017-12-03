data=as.matrix(read.table("day2_data",sep="\t",header=F))

## Part 1
d=0
for(i in 1:nrow(data)){
  d=d+max(data[i,])-min(data[i,])
}
print(d)

## Part 2
checksum = 0
for(i in 1:nrow(data)){
  pair=expand.grid(x=data[i,],y=data[i,])
  for(j in 1:nrow(pair)){
    if(pair[j,1]%%pair[j,2]==0 & pair[j,1]/pair[j,2]!=1) checksum=checksum+pair[j,1]/pair[j,2]
  }
}  
print(checksum)
