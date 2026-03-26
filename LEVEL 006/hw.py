
#2) კომენტარების სახით ახსენით რა არის input-ი და output-ი, მოიყავნეთ შესაბამისი მაგალითები.

#3) შექმენით ცვლადი, რომელშიც შეინხავთ input ინსტრუქციით შემოტანილ მნიშვნელობას, შემდეგ შეამოწმებთ თუ რა ტიპის მონაცემი ინახება ამ ცვლადში და დაპრინტავთ.

#4) თიოთეული მონაცემთა ტიპისთვის (str,int,float), შექმენით 5 ცვლადი და დაუწერეთ კომენტარი თუ რომელ მონაცემთა ტიპს ინახავს ცვლადი.

#5) აიღეთ 3 ცვლადი, შეინახეთ განსხავებული მონაცემთა ტიპები (str,int,float), შემდეგ type ინსტრუქციის გამოყენებით შეამოწმეთ, თუ რომელ მონაცემთა ტიპს ინახავს ცვლადი.

#6) მომხმარებელს შემოატანინეთ ორი სიტყვა, შეინახეთ ისინი ცვლადებში, მოახდინეთ მათი კონკატინაცია და დაბეჭდეთ.

#7) მომხმარებელს შემოატანინეთ 5 რიცხვი სხვადასხვა დამოუკიდებელი input-ების სახით, თქვენი დავალებაა დაბეჭდოთ მათი საშუალო არითმეტიკული.

#8) მომხმარებელს შემოატანინეთ სახელი, გვარი, ასაკი, სიმაღლე, წონა და ამ მონაცემების გამოყენებით დაბეჭდეთ ერთი დიდი წინადადება.

#2)input-არის მაგალითად და მოკლედ რომ ვთქვათ ნივთი რომელლსაც ვმართავთ და ვაკონთროლებთ ანუ სემავალი ინფოირმაცია
#output-არის რასაც ჩვენით ვერ ვაკონტროლებთ მაგალითად დინამიკი მონიტორი მაგრამ პითონში მას სულ სხვა ახსნილობა აქვს იგი მოიაზრება როგორც გამავალ ინფორმაციად

#3)
name=input("enter your name:")
print(type(name))

#4)
string="hello world"
 #tipe str
integer=15
#type int
integer2=114
#type int
float=12.1
#type float
string2="goodbye"
#type str

#5)
location="tbilisi"
print(type(location))
age=9
print(type(age))
fav_nummber=7.9
print(type(fav_nummber))
#6)
name=input("enter your name :0")
name2=input("enter your name :)")
print( name + name2 )
#7)
num1=input("enter your nummber:")
print(num1)
num2=input("enter your nummber:")
print(num2)
num3=input("enter your nummber:")
print(num3)
num4=input("enter your nummber:")
print(num4)
print(num1 + num2+num3+num4 / 5)

#8)
name=input("enter your name:")
print(name)
last_name=input("enter your last name:")
print(last_name)
age=input("enter your age:")
print(age)
height=input("enter your height:")
print(height)
weight=input("enter your weight:")
print(weight)
print(f"my name is , {name} last name is {last_name} my age is{age} my height is {height} my weight is {weight}" )
