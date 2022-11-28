person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }


print(f"a) {person}")
print(person["name"])
print(person["hobby"])


print(f"d) przed zmiana {person}")
person["surname"]= "Nowak"
print(f"d) po zmianie {person}")

print(f"e) przed zmiana {person}")
person["married"] = False
print(f"e) po zmianie {person}")

person["hobby"]+= ["bicycle"]
print(f"f) {person}")

person["gender"]= False
print(f"g) {person}")

person["height"] = 180
print(person)

person["phone"]["workphone"]="313131444"
print(person)
