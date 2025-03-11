# 2) კომენტარის სახით ჩამოწერეთ თუ რა განსხვავებაა set-ებსა და list-ებს შორის.
    #set --> კოლექცია რომელიც არის დაულაგებელი,შეუცვლელი და არ დაიშვება ორი ან მეტი ერთნაირი ელემენტი




# 4) შექმენით set, რომელშიც შენახული გექნებათ Fast food საკვები პროდუქტები. შემდეგ კი ამოშალეთ ყველა პირვანდელი ელემენტები set-იდან, და მათ ნაცვლად დაამატეთ ჯანსაღი საკვები პროდუქტები.
fast_foods = {"burger", "fries", "pizza", "hotdog", "nuggets"}

fast_foods.clear()

fast_foods.add("apple")
fast_foods.add("banana")
fast_foods.add("salad")
fast_foods.add("chicken breast")
fast_foods.add("nuts")

print(fast_foods)


