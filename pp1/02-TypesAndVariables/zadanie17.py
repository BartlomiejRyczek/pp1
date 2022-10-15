print("Podaj swój wzrost w centymetrach: ")
wzrost=float(input())
x=(wzrost*0.032808399) #wzrost w stopach
y=(wzrost*0.393700787) #wzrost w calach

stopy=(round (x,3))
cale=(round(y,2))

print(f"Twój wzrost w stopach wynosi {stopy}, a w calach {cale}")
