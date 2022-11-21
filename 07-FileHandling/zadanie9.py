with open('numbers.txt', 'r') as f:
    result = sum(map(int, f))

print(result)


f= open('numbers.txt', 'r')
sum = 0
for line in f:
    print(line, end="")
    sum=sum+int(line)

print(sum)