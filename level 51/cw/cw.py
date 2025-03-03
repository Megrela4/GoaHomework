# 1) კომენტარის სახით ახსენით, თუ რა განასხვავებს tuple-ებს List-ებისგან.
    # პირველი განსხვავება არის სინტაქსი
    # მეორე განსხვავებაა list-ების შეცვლა შეგვიძლია მაგრამ tuple-ბის არა


# 2) შექმენით tuple, რომელიც შეიცავს თქვენს 5 საყვარელ ფილმს, შემდეგ კი დაბეჭდეთ პირველი და ბოლო ელემენტი ამ tuple-დან.
favorite_movies = ("Random", "randoM", "rAndom", "random", "raNdom")
first_movie = favorite_movies[0]
last_movie = favorite_movies[-1]
print(first_movie)
print(last_movie)


# 3) შემენით Tuple, რომელშიც შეინახავთ კვირის დღეებს და მოახდინეთ მათი unpacking (destruction),რათა მიანიჭოთ თითოეული ელემენტი ცალკეულ ცვლადებს და დაბეჭდეთ ეს ცვლადები.
weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
monday, tuesday, wednesday, thursday, friday, saturday, sunday = weekdays
print(monday)
print(tuesday)
print(wednesday)
print(thursday)
print(friday)
print(saturday)
print(sunday)


# 4) შექმენით tuple, რომელიც შეიცავს რამდენიმე ელემენტს. შემდეგ შეამოწმეთ, შეიცავს თუ არა ეს tuple კონკრეტულ ელემენტს
fruits = ("ვაშლი", "ბანანი", "ატამი", "ფორთოხალი")
if "ბანანი" in fruits:
    print("ბანანი არის tuple-ში")
else:
    print("ბანანი არ არის tuple-ში")


# 5) მოცემულია 
# tuple = ("banana", "cherry", "strawberry", "raspberry")
# (first, *second, third) = fruits

# რას გამოიტანს შემდეგი კოდი?
# print(first) "banana"
# print(second) ["cherry", "strawberry"]
# print(third)  "raspberry"