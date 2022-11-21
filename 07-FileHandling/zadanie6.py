file = open('countries.txt','r', encoding="UTF-8") #encoding wpływa na poprawny zapis polskich znakow
file_content = file.read()
print( file_content )
file.close()
