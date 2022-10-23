from random import randrange
x=30
podzielnaprzez3=x%3==0
podzielnaprzez5=x%5==0
podzielnaprzez3i5=podzielnaprzez3 and podzielnaprzez5
for x in x:
    if podzielnaprzez3:
        print(f"THREE") 
    if podzielnaprzez5:
        print(f"FIVE")
    if podzielnaprzez3i5:
        print(f"BINGO")  
#if podzielnaprzez3:
    #print(f"THREE")
#if podzielnaprzez5:
    #print("FIVE")
#if podzielnaprzez3 and podzielnaprzez3i5:
    #print("BINGO")

