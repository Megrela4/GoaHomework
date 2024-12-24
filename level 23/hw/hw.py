# 1) მომხმარებელს შემოატანინეთ მისი სახელი დიდი ასოებით და შეინახეთ ცვლადში სახელად name და .lower() ფუნქციის მეშვეობით გადააქციეთ ცვლადის მნიშვნელობა  პატარა ასოებად.
name = input("your name in upper case: ").upper()
name = name.lower()
print(name) # using print to test if it worked



# 2) ცვლადში შეინახეთ თქვენი გვარი პატარა ასოებით, შემდეგ .upper() ფუნქციის მეშვეობით გადააქციეთ ცვლადის მნიშვნელობა  დიდ ასოებად.
lastname = "megrelishvili"
lastname = lastname.upper() # using print to test if it worked



# 3) ცვლადში შეინახეთ სტრინგი პატარა ასოებით, შემდეგ .capitalize() ფუნქციის მეშვეობით გადააქციე პირველი ასო დიდ ასოდ.
random = "phone"
random = random.capitalize()
print(random)  #using print to test if it worked



# 4)ცვლადში შეინახეთ რაიმე სტრინგი,შემდეგ find() ფუნქციის მეშვეობით იპოვეთ რომელ ინდექსზეა კონკრეტული ასო
random_string = "airplane"
print(random_string.find("r"))
