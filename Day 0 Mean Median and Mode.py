# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
t = int(input())

val = list(map(int,input().rstrip().split(' ')))
size = t
val = sorted(val)
print(sum(val)/size) #mean

#median
if size%2==0: print(0.5*( val[int(size/2)] + val[int(size/2)-1] ))
else: print(val[int(size/2)-1])

#mode
from collections import Counter
value = Counter(val).most_common(1)[0][0]
#Counter iterates through all values in val and most_common searches for most appearing values.
#1 for value with highest frequency i.e. mode.
#[0][0] for formatting to get single value.
print(value)


'''
Alternatively for mode, you can use
mode = max(set(val), key=list.count), where val is list, no need to import any basic package!'''
