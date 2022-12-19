import random

class Arrays():

    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)
            
    def a(number_of_array_elements, value_of_array_elements):
        array=[]
        for x in range(0,number_of_array_elements):
            array.append(value_of_array_elements)
        return array

    def b(number_of_elements, value_from, value_to):
        array=[]
        for i in range(number_of_elements):
            x=random.randint(value_from, value_to)
            array.append(x)
        return array
    
    def c(array, value_from, value_to):
        licznik=0
        for i in array:
            if i>value_from and i<=value_to:
                licznik+=1
        return licznik

print(Arrays.a(5,5))
print(Arrays.b(5,1,9))
print(Arrays.c([1,2,3,4,5,7,8],0,9))
