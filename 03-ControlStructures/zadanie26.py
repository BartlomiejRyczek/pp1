x='0805'
y=0
while True:
    line = input('Podaj liczbę: ')
    if line == '0805':
        print("PIN jest poprawny")
        break
    if line!= '0805':
        print("PIN jest niepoprawny")
        y=y+1
    if y==3:
        print("Twoje konto zostało zablokowane")
        break