def suma(n):
    if n==1:
        return 1
    if n > 1:
        return n + suma(n-1)
for x in range (0, 11):
    print( f"{x} = {suma(x)}" )
