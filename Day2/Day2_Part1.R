INPUT = read.table("AoC_day2.csv", sep=",", header=FALSE) 
result_sum = 0
for (row in 1:length(INPUT[,1])) {
    result_sum = result_sum + max(INPUT[row,]) - min(INPUT[row,])
}
print(result_sum)
