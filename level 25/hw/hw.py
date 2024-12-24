# 1)შექმენით ცარიელი სია და for ციკლის მეშვეობით ჩაამატეთ ყველა ლუწი რიცხვი 0დან 200მდე, ბოლოს დაბეჭდეთ სია.
list = []
for i in range(200):
    if i % 2 == 0:
        list.append(i)        
print(list)


# 2)შექმენით ცარიელი სია და for ციკლის მეშვოებით მომხმარებელს შეეკითხეთ მისი top 5 საყვარელი სახელი (ანუ ხუთჯერ input).
favourite_movies = []
for i in range(5):
    favourite_movies.append(input("favourite movie:"))
print(favourite_movies)


# 3)შექმენით სია 10 ელემენტით და გამოიტანეთ მხოლოდ კენტ ინდექსზე მდგომი ელემენტები.
random = [12, 32, 54, 2345, 564, 23, 1, 99, 654, 777]
for i in range(len(random)):
    if i % 2 == 1:
        print(random[i])


# 4)შექმენით ცვლადი რომელშიც შენახული იქნება სტრინგი შემდეგ კი გაიგეთ ამ სტრინგის სიმბოლოების რაოდენობა.
string = "Hello"
print(len(string))


# 5)შექმენით სია შემდგარი 5 ელემენტისგან, მომხმარებელს შემოატანინეთ რიცხვი და სიიდან ამოაგდეთ შემოტანილ რიცხვის ინდექსზე მდგომი ელემენტი.
list2 = ["second", "first", "name", "random", "unknown"]
list2.pop(-1)
list2.append(int(input("random number:")))
print(list2)


# 6)შექმენით სია და დაბეჭდეთ ამ სიის სიგრძე.
list3 = []
for i in range(11):
    list3.append(i)
print(len(list3))


