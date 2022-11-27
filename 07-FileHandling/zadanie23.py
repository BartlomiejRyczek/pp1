import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures =re.findall("\d{2}",message)
x=([int(y) for y in temperatures])
suma=sum(x)
srednia=suma/len(x)

print(srednia)