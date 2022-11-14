array = [2,3,7,5,4]

print("a)", array)
print("b)", len(array))
print("c)",array[0])
print("d)",array[1])
print("e)",array[-1])
print("f)",array[len(array)-2])
print("g)",array[0]+array[-1])
print("h)",array[int(len(array)/2)])

print("i)")
for i in array:
    print(i, end=" ")

print("")
print("j)")


for i in array[:3]:
    print(i, end=" ")
#lub
print(" ")
for i in range(0, int(len(array)/2)+1):
    print(array[i], end=" ")