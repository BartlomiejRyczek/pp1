def median(array):
    i=0
    for x in array:
        i+=x
    return i/len(array)

a=[1,0,9,4,6]
b=[6,8,3,1,0,5,7]

print(median(a))
print(median(b))
