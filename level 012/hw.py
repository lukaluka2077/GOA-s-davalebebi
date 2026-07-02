# 2) for ციკლი 0-დან 38-ის ჩათვლით
for i in range(0, 39):
    print(i)
# 3) for ციკლი 30-დან 40-მდე

for i in range(30, 41):
    print(i)
# 4) for ციკლი 12-დან 120-მდე
for i in range(12, 121):
    print(i)
# 5) სახელის 18-ჯერ დაბეჭდვა
for i in range(18):
    print("luka")
# 6) 10-დან 100-მდე step=3
for i in range(10, 101, 3):
    print(i)
# 7) ხილის დაბეჭდვა ნუმერაციით
for i in range(1, 31):
    print(f"{i} ფორთოხალი")
# 7) ასაკის შეყვანა 13-ჯერ
for i in range(13):
    age = input(f"შეიყვანეთ თქვენი ასაკი ({i+1}/13): ")
    print(f"შეყვანილი ასაკი: {age}")
# 8) while loop-ით სახელის 10-ჯერ დაბეჭდვა
count = 0
while count < 10:
    print("nika")
    count += 1
# 9) while loop-ით 0-დან 24-მდე დათვლა
i = 0
while i <= 24:
    print(i)
    i += 1
    # 10) დამატებითი მაგალითები

# მაგალითი 1: ჯამის გამოთვლა
total = 0
for i in range(1, 11):
    total += i
print("1-დან 10-მდე რიცხვების ჯამი:", total)

# მაგალითი 2: while-ით ლუწი რიცხვები
num = 2
while num <= 20:
    print(num)
    num += 2

# მაგალითი 3: შებრუნებული დათვლა
for i in range(10, 0, -1):
    print(i)
print('i')

# მაგალითი 4: ცხრილის დაბეჭდვა (მრავლობითი ცხრილი)
for i in range(1, 11):
    print(f"5 * {i} = {5 * i}")
