polska={
    "Nazwa": "Polska",
    "Populacja": 38000000
}

niemcy={
    "Nazwa": "Niemcy",
    "Populacja": 80000000
}
czechy={
    "Nazwa": "Czechy",
    "Populacja": 8000000
}
hiszpania={
    "Nazwa": "Hiszpania",
    "Populacja": 56000000
}

francja={
    "Nazwa": "Francja",
    "Populacja": 68000000
}

uk={
    "Nazwa": "Wielka Brytania",
    "Populacja": 68000000
}

ar=[polska, niemcy, czechy, hiszpania, francja, uk]
i=0
while i < len(ar):
    for key, value in ar[i].items():
        print(key,":", value)
    i+=1