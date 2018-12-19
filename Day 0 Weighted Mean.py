# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
val = list(map(int,input().rstrip().split(' ')))
weight = list(map(int,input().rstrip().split(' ')))

mean = sum(val[i]*weight[i] for i in range(t))/sum(weight) #Weighted mean
print(round(mean,1)) #1-digit precision
