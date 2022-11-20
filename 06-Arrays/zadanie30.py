def minmax(array):
    max=array[0]
    min=array[0]
    for i in array:
        if i>max:
            max=i
        if i<min:
            min=i
    return min,max

Array = [4,2,8,4,7,9,5]
print(minmax(Array))