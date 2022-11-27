import csv


with open('students.txt', 'r') as csvfile:
    csv_reader=csv.DictReader(csvfile)
    
    for line in csv_reader:
        print(line['first_name'], line['last_name'], line['email'])
    
 