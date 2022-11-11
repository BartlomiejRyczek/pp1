def mounth(n):
    if n==1:
        return "Styczen"
    if n==2:
        return "Luty"
    if n==3:
        return "Marzec"
    if n==4:
        return "Kwiecień"
    if n==5:
        return "Maj"
    if n==6:
        return "Czerwiec"
    if n==7:
        return "Lipiec"
    if n==8:
        return "Siepień"
    if n==9:
        return "Wrzesień"
    if n==10:
        return "Październik"
    if n==11:
        return "Listopad"
    if n==12:
        return "Grudzien"
    if n>12:
        return "Nie ma takiego miesiaca"
        
print(mounth(7))