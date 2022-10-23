from calendar import c
from lzma import FILTER_LZMA2



def fib(n):
    a=0
    b=1
    print(a)
    print(b)
    for x in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)
fib(20)