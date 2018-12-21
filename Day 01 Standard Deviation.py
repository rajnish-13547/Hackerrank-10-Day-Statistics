# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
val = list(map(int,input().rstrip().split(' ')))

size = len(val)
val = sorted(val)
mean = sum(val)/size

import math
out =[]
for values in val:
    out.append((values-mean)**2)

std = round(math.sqrt(sum(out)/size),1)
print(std)
