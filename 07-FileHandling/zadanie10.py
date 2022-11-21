file = open('ja.txt','w')
file.write("Bartek\n")
file.write("Ryczek\n")
file.write("Uniwerstytet Ekonomiczny w Krakowie\n")
file.write("Informatyka Stosowana\n")

file = open('ja.txt','r', encoding="UTF-8") #encoding wpływa na poprawny zapis polskich znakow
file_content = file.read()
print( file_content )
file.close()
