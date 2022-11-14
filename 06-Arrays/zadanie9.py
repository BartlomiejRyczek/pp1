ar = ["Genowefa","Onufry","Celestyna", "Alojzy", "Pankracy"]

longest=len(ar[0])
zmienna=ar[0]

for x in ar:
    if(len(x)>longest):
        longest=len(x)
        zmienna=x
    
print(zmienna)