wzrost=input("Podaj Twój wzrost w metrach: ")
wzrost1=float(wzrost)
waga=input("Podaj Twoją wagę w kilogramach: ")
waga1=float(waga)

#bmi = masa/wzrost^2

potegowanie=(wzrost1**2)

bmi=waga1/potegowanie
x=round(bmi, 2)

print(f"Twój BMI index wynosi: {x}")