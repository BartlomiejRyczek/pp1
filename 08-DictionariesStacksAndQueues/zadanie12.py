import json


movie = {
    "Nazwa":"XYZ",
    "Rok_produkcji":2001,
    "Rezyser":"Jacek Nowak",
    "Oscar":True,
    "aktorzy":["Anna Kowalska", "Mateusz Kowalczyk"]
}


out_file = open("film.json","w")

json.dump(movie, out_file, indent=4)
out_file.close()
