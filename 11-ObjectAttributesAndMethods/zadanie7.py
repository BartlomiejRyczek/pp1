class Student():
    
    # class variables
    uniwersytet = "UEK Kraków"
    id=100000
    
    def __init__(self, name, surname, field_of_study):
        self.name = name
        self.surname= surname
        self.field_of_study=field_of_study

    def __str__(self):
        Student.id+=1
        return f"{self.name} {self.surname}({Student.id}),{self.field_of_study}, {Student.uniwersytet}"


p = Student("Anna", "Maj", "Applied Informatics")
print(p)
p2 = Student("Jan","Kowalski","Applied Informatics")
p3 = Student("Kacper","Nowak","Applied Informatics")
print(p2)
print(p3)