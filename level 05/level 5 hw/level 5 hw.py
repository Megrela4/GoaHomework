# დავალება 1)მომხმარებელს შემოატანინეთ float სახის რიცხვი და შემდეგ ეგ რიცხვი გაყავით floor division-ის დახმარებით რომ იყოს integer და არა float

float = float(input("num:" ))
print (int(float // 2))


# დავალება 2)მოხმარებელს შემოატანინეთ თავის სახელი,გვარი,ასაკი,ჰობბი და ბალანსი შემდეგ ეს ყველაფერი დაბეჭდეთ print-ის საშუალებით

name = input("name: ") #სახელი
lastname = input("lastname: ") #გვარი
age = input("age: ") #ასაკი
hobby = input("hobby: ") #ჰობბი
print ( "my" + " " + "name" + " " + "is" + " " + name + " " + lastname + " " + "my" + " " + "age" + " " + "is" + " " + age + " " + "i" + " " + "love" + " " + hobby )


# დავალება 3)გააკეთეთ 5 5-ი მაგალითი %-ზე და floor division-ზე //

#floor division ( // )
print(int(10.3 // 2))
print(int(3.4 // 3))
print(int(16.9 // 7))
print(int(19.4 // 3))
print(int(37.1 // 3))

#modulus (%)
print(6 % 5)
print(5 % 2)
print(8 % 3)
print(11 % 2)
print(17 % 6)


# დავალება 4)მოხმარებელს შემოატანინეთ რიცხვი და მაგ რიცხვს გამოაკელით 20 და გაამრავლეთ 3 ზე

number = int(input("number:" ))
print(number - 20)
print(number * 3)


# დავალება 5)მოხმარებელს შემოატანინეთ რიცხვები ანუ num,num1,num2...და ასე შემდეგ და საბოლოოდ გამოითვალეთ მაგ რიცხების საშუალო არითმეტიკული
# მაგალითად:2, 2, 2 = 2 + 2 + 2 = 6 / 3 = 2 ანუ რიცხვების ჯამი გავყოთ რაოდენობაზე(მინიმუმ 3 რიცხვის ცვლადი გქონდეთ შექმნილი)

num1 = int(input("num1:" ))
num2 = int(input("num2:" ))
num3 = int(input("num3:" ))
num4 = int(input("num4:" ))
num5 = int(input("num5:" ))

print(( num1 + num2 + num3 + num4 + num5) / 5)





