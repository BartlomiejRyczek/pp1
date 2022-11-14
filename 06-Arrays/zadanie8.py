ar=[-15,8,-31,47,-2,19]

max=ar[0]
min=ar[0]

for i in ar:
    if i>max:
        max=i
    if i<min:
        min=i
print(max, min)