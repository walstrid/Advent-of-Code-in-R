## Part 1

v = c(4,1,15,12,0,9,9,5,5,8,7,3,14,5,12,3)
mem=list()
pos=rep(1:16,3)
n=0
while(!(list(v)%in%mem)){
  mem=append(mem,list(v))
  mxpos=which.max(v)
  mx=max(v)
  v[mxpos]=0
  for(i in pos[(mxpos+1):(mxpos+mx)]){
    v[i]=v[i]+1
  }
  n=n+1
}
n

## Part 2
mem=append(list(v),mem)
n-which(duplicated(mem))+2 # on enlève 2 à la position dupliquée car on compte le vecteur initial + celui ajouté au début

