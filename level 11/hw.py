# 2)შექმენით 8 ცვლადი სადაც შეინახავთ ყველა შესაძლო ლოგიკური ოპერატორის მაგალითს (4 ცალი or / 4 ცალი and)
# ver mivxvdi davalebis pirobas


# 3)მომხმარებელს შემოატანინეთ მისი სახელი, შემოატანინეთ მისი ასაკი, ასევე სიმაღლე და შეამოწმეთ თუ მომხმარებლის ასაკი მეტია 18 და მისი სახელი უდრის თქვენს სახელს და ასევე მისი სიმაღლე მეტია 1.80-ზე
name = input("your name: ")
my_name = "nika"
if name == my_name:
    print("same name")
else:
    print("nice name")


age = int(input("your age: "))
if age >= 18:
    print("Over 18")
else:
    print("Not 18")


height = float(input("your height: "))
if height > 1.80:
    print("tall")
elif height > 1.70 and height < 1.80:
    print("normal height")
else:
    print("short")


