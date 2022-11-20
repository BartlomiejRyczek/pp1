def bubbleSort( theSeq ):
    n = len( theSeq )

    for i in range( n - 1 ) :
        flag = 0

        for j in range(n - 1) :
            
            if theSeq[j] > theSeq[j + 1] : 
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp
                flag = 1

        if flag == 0:
            break

    return theSeq


eo=[6,8,1,2,3,55,4]
ko=[88,6,6,3,11,25,2,3]
gf=[1,2,3,515,32,582,0,25]
result = bubbleSort(eo)
result1 = bubbleSort(ko)
result2 = bubbleSort(gf)
print(result)
print(result1)
print(result2)