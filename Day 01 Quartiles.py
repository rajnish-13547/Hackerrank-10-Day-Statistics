size = int(input())
val = list(map(int,input().rstrip().split(' ')))

def median (arr):
    size_1 = len(arr)
    if size_1%2 ==0:
        med = (arr[int(size_1/2)]+arr[-1+int(size_1/2)])/2
    else:
        med = arr[int(size_1/2)]

    return med

if size%2==0: #Assuming size = len(val)
    val1 = val[:int(size/2)]
    val2 = val[int(size/2):]
else:
    val1 = val[:int(size/2)]
    val2 = val[1+int(size/2):]

print(median(val1))
print(median(val))
print(median(val2))
