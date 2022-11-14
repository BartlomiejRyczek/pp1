ar = [1,2,3,4,5]

print(ar[0]-1)
ar[0] = ar[0]-1
print(ar[-1]+4)
print(ar[2]*2)


for i in ar:
    i+=3
    print(i, end=" ")

for i in range(0, len[ar]):
    ar[i]+=3
    print(i, end=" ")