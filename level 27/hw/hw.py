# 1)შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა ორი რიცხვი შემდეგ კი გამოიტანეთ ამ რიცხვების ჯამი.
def math(num1, num2):
    print(num1 + num2) #from this time use return not print like example: return num1 + num2

math(123, 456)


def odd_even(num):
    if num % 2 == 0:
        print("its even")
    else:
        print("its odd")

odd_even(12)   


# 3)შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა რიცხვი შემდეგ კი მან უნდა დაგვიბრუნოს ეს რიცხვი დადებითია თუ უარყოფითი.
def number(num):
    if num < 0:
        print("უარყოფითი")
    
    else:
        print("დადებითია")

number(13)


# 4)შექმენით ფუნქცია, რომელსაც არგუმენტად გადაეცემა სახელი და დაბეჭდავს მისთვის მიესალმებას (მაგალითად: "Hello Giorgi"). გამოძახეთ ეს ფუნქცია 2-ჯერ და გადაეცით სხვადასხვა სახელი.
def name(name):
    print("Hello", name.capitalize())

name("nika")
name("vano")


# 5)შექმენით ფუნქცია, რომელიც იღებს ორ სტრინგს და მოახდინეთ კონკატენაცია.
def concatination(str1, str2):
    print(str1 + str2)

concatination("air", "plane")


