x=int(input("Podaj wiek psa w ludzkich latach: "))

if x<=2:
    psi_wiek=x*10.5
    print(f"Pies ma {psi_wiek} psich lat")

else:
    psi_wiek = 21 +(x-2)*4
    print(f"Wiek psa w psich latach wynosi {psi_wiek} ")
