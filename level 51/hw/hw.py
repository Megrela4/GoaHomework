# 1)გადახედეთ ამ რესურსებს:
# https://www.w3schools.com/python/python_tuples.asp
# https://www.w3schools.com/python/python_tuples_access.asp
# https://www.w3schools.com/python/python_tuples_update.asp
# https://www.w3schools.com/python/python_tuples_unpack.asp
# https://www.w3schools.com/python/python_tuples_loop.asp

# 2) შემენით tuple, რომელშიც შეინახავთ საყიდლების სიას და მოახდინეთ მათი unpacking (დაშლა),რათა მიანიჭოთ თითოეული ელემენტი ცალკეულ ცვლადებს და დაბეჭდეთ ეს ცვლადები.
food = ("Potato", "Apple", "Cherry", "Carrot", "Butter",)
potato, apple, cherry, carrot, butter = food
print(potato)
print(apple)
print(cherry)
print(carrot)
print(butter)

# 3) შექმენით tuple და შეინახეთ Fast food პროდუქტები. შემდეგ შეცვალეთ ეს tuple და მათში ჩაამატეთ ჯანსაღი საკვები პროდუქტები.

# 4) კომენტარის სახით ახსენით, თუ რა ფუნქციას ასრულებს Asterisk და როგორ აღინიშნება ის.

# 5) მოცემულია შემდეგნაირი tuple:

# months = ("January", "February", "March", "April", "May")
# (first, second, third, fourth*)= months

# რას გამოიტანს მოცემული კოდი?
# print(first) = January
# print(second) = February
# print(third) = March
# print(fourth) = ["April", "May"]