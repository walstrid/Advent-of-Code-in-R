data = read.table("day2_data",sep="x",header=F)
colnames(data) = c("l","w","h")

## Part 1
surf = function(x){
  v = c(2*x[1]*x[2],2*x[2]*x[3],2*x[1]*x[3])
  sum(v)+min(v)/2
}
sum(apply(data,1,surf))

## Part 2
len = function(x){
  sum(sort(x)[-3])*2 + prod(x)
}
sum(apply(data,1,len))
