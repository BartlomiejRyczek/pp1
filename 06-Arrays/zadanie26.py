ar = [5,1,9,6,1]

a = max(ar)
b = ar[0]
for i in ar:
    if i>b and i!=a:
        b=i
print(b)