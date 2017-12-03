length(INPUT) #=2000
size / 2 #=1000
for (i in 1:1000) {
  if (INPUT[i] == INPUT[i+1000]) {result_sum = result_sum + INPUT[i]
  }
}
count=0
for (i in 1001:2000) {
  count=count+1
  if (INPUT[i] == INPUT[count]) {result_sum = result_sum + INPUT[i]
  }
}
print(result_sum)
