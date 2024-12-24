
# FOR LOOP

# 1)გამოიტანეთ რიცხვები 0-დან 10-ის ჩათვლით
for i in range(11):
    print(i)

# 2)გამოიტანეთ რიცხვები 50-დან 150-მდე
for i in range(50, 151):
    print(i)

# 3)გამოიტანეთ მხოლოდ ლუწი რიცხვები 200-დან 500-მდე
for i in range(200, 501, 2):
    print(i)

# 4)გამოიტანეთ კენტი რიცხვები 0-დან 50-მდე
for i in range(1, 51, 2):
    print(i)


# 5)მომხმარებელს შემოატანინეთ მისი გვარი და გამოიტანეთ ამ გვარის თითოეული ასო ცალცალკე
last_name = input("last name: ")
for letter in last_name:
    print(letter)




# WHILE LOOPS

# 1)გამოიტანეთ რიცხვები 10-დან 15-მდე
number = 10
while number <=15:
    print(number)
    number += 1

# 2)გამოიტანეთ რიცხვები 50-დან 0-მდე
second_number = 50
while second_number >= 0:
    print(second_number)
    second_number -= 1

# 4)გამოიტანეთ მხოლოდ ლუწი რიცხვები 10-დან 70-მდე
third_number = 10
while third_number <= 70:
    print(third_number)
    third_number += 2

# 5)გამოიტანეთ კენტი რიცხვები 25-დან 55-მდე
fourth_number = 25
while fourth_number <= 55:
    print(fourth_number)
    fourth_number += 2