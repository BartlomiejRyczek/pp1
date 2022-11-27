import re

with open("grades.txt") as f:
    for line in f:
        print(line, end="")
        
oceny=re.findall('[0-9]+[\.,][0-9]', line)
x=([float(y) for y in oceny])
suma=sum(x)
srednia=suma/len(x)

print(f"Średnia ocen ucznia wynosi {srednia}")

