def power(x,n):
    if n==1:
        return x
    if n==0:
        return 1
    if n>0:
        xn=x*x**(n-1)
    return xn

print(power(5,3))

