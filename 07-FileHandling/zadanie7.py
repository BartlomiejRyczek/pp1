file = open('countries.txt','r', encoding="UTF-8")
x=1
for line in file:
     print(x, line, end="")
     x+=1
file.close()