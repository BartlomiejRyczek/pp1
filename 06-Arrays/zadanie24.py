arr = [1,1,1,3,6,5,4,2,3,5]
print(arr)

for i in arr:
    if arr.count(i)==1:
        print(i, end=" ")