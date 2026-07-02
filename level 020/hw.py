#1)
numbers_step = [5, 10, 15, 20, 25, 30, 35, 40]
every_second = numbers_step[::2]
print(every_second)
#2)
fruits = ["ვაშლი", "მსხალი", "ატამი", "ბალი", "ყურძენი", "ბანანი", "ფორთოხალი"]


middle_fruits = 'fruits[2:5]'

print(middle_fruits)  
#3)
mixed_nums = [12, 45, 8, 33, 91, 24, 10, 77]

for num in ('mixed_nums'):
   
    if num % 2 == 0:
        print(num)

print("გამარჯობა!")


#4)
def greet(name): 
    print(f"გამარჯობა, {name}!")

greet("გიორგი") 
greet("ნინო")  



def add_numbers(a, b):
    result = a + b
    print(result)

add_numbers(5, 10)   
add_numbers(100, 25) 

def greet_with_default(name="სტუმარო"):
    print(f"გამარჯობა, {name}!")

greet_with_default()          

greet_with_default("ლუკა")     
