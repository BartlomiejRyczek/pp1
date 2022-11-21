ar=['Hobbit', 'Zielona Mila', 'Madagaskar', 'Wladca Pierscieni', "Iron man"]
file = open('filmy.txt')
for title in ar:
    file.write(f"{title}\n")
file.close()