# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input())
val = list(map(int,input().rstrip().split(' ')))
freq = list(map(int,input().rstrip().split(' ')))
out = []
for i in range(len(val)):
    for j in range(freq[i]): out.append(val[i])

val = sorted(out)
size = len(val)

def median (arr):
    size_1 = len(arr)
    if size_1%2 ==0:
        med = (arr[int(size_1/2)]+arr[-1+int(size_1/2)])/2
    else:
        med = arr[int(size_1/2)]

    return float(med)

if size%2==0: #Assuming size = len(val)
    val1 = val[:int(size/2)]
    val2 = val[int(size/2):]
else:
    val1 = val[:int(size/2)]
    val2 = val[1+int(size/2):]
print((median(val2)-median(val1)))
