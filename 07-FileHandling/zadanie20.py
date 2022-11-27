import random

with open('zadanie20.txt','w') as f:
    for x in range(50):
        f.write(str(random.randint(100,999))+"\n")
        
