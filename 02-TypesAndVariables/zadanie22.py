x=input("Podaj zapłaconą kwotę: ")
kwota=float(x)

vat=kwota*0.23

vatzaokraglony=round(vat, 2)

print(f"Zapłacona kwota: {kwota}")
print(f"VAT 23%: {vatzaokraglony}")
