## Part 2

a=347991
m=matrix(NA,nrow=20,ncol=20)
mx=1
x0=y0=x=y=20/2
m[y0,x0]=1
adj=function(x,y){m[(y-1):(y+1),(x-1):(x+1)]}
while(m[y,x]<a){
  while(x<x0+mx){
    x=x+1
    m[y,x]=sum(adj(x,y),na.rm=TRUE)
  }
  while(y>y0-mx){
    y=y-1
    m[y,x]=sum(adj(x,y),na.rm=TRUE)
  }
  while(x>x0-mx){
    x=x-1
    m[y,x]=sum(adj(x,y),na.rm=TRUE)
  }
  while(y<y0+mx){
    y=y+1
    m[y,x]=sum(adj(x,y),na.rm=TRUE)
  }
  mx=mx+1
}

min(m[which(m>a)])

