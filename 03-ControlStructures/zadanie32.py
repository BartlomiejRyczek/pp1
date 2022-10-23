#n=7
#for i in range(n):
    #m = i+1
    #for j in range(n):
       # print(m, end=" ")
        #m=m+1
   #print()


rows = int(input("Enter the number of rows: "))  
for i in range(0, rows):  
    for j in range(rows, 0, -1):  
        print(j, end=' ')  
    print()  