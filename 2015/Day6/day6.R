data=readLines("day6_data")
data=strsplit(data,split=" ")

## Part 1
m=matrix(0,nrow=1000,ncol=1000)
v=x1=x2=c()
for(i in 1:length(data)){
  excor = function(x,y){
    v=c(data[[i]][x],data[[i]][y])
    strsplit(v,split=",")
  }
  if("turn"%in%data[[i]]){
    v=excor(3,5)
    x1=v[[1]]
    x2=v[[2]]
    if("on"%in%data[[i]]){m[x1[1]:x2[1],x1[2]:x2[2]]=1}
    else{m[x1[1]:x2[1],x1[2]:x2[2]]=0}
  }
  else{
    v=excor(2,4)
    x1=v[[1]]
    x2=v[[2]]
    for(w in x1[1]:x2[1]){
      for(z in x1[2]:x2[2]){
        if(m[w,z]==0){m[w,z]=1} else{m[w,z]=0}
      }
    }
  }
}
length(which(m[]==1))

## Part 2
m=matrix(0,nrow=1000,ncol=1000)
v=x1=x2=c()
for(i in 1:length(data)){
  excor = function(x,y){
    v=c(data[[i]][x],data[[i]][y])
    strsplit(v,split=",")
  }
  if("turn"%in%data[[i]]){
    v=excor(3,5)
    x1=v[[1]]
    x2=v[[2]]
    if("on"%in%data[[i]]){m[x1[1]:x2[1],x1[2]:x2[2]]=m[x1[1]:x2[1],x1[2]:x2[2]]+1}
    else{
      for(w in x1[1]:x2[1]){
        for(z in x1[2]:x2[2]){
          if(m[w,z]==0){m[w,z]=0} else{m[w,z]=m[w,z]-1}
        }
      }  
    }
  }
  else{
    v=excor(2,4)
    x1=v[[1]]
    x2=v[[2]]
    m[x1[1]:x2[1],x1[2]:x2[2]]=m[x1[1]:x2[1],x1[2]:x2[2]]+2
  }
}
sum(m)
