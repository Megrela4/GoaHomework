# 1)კომენტარის მეშვეობით ახსენით .lower() / .upper() / .capitalize() / .find() ფუნქციების დანიშნულება

# .upper()  # ასოების გადიდება

# .lower()  # ასოებს დააპატარავებს

# .capitalize() # პირველს გაადიდებს (პირველ ასოს) დანარჩენს აპატარავებს

# .find() #ასოს ინდექსის პოვნა




# 2)მომხმარებელს შემოატანინეთ მისი გვარი და შეამოწმეთ, თუ გვარის პირველი ასო არის დიდი ასო, მაშინ დაუბეჭდეთ "Hello", თუ არ არის მაშინ დაუბეჭდეთ "Bye"

surname = input("your surname: ")
if surname == surname.capitalize():
    print("Hello")
else:
    print("Bye")



# 3)მომხმარებელს შემოატანინეთ სახელი, შემდეგ შემოატანინეთ ასო და თუ ამ სახელში ეს ასო არიქნება, მაშინ გამოუტანეთ "Can't find character", თუ იქნება მაშინ გამოუტანეთ "found it" და გვერდზე მიუწერეთ ამ ასოს ინდექსი
name = input("your name:")
letter = input("one letter:")
if name.find(letter) > -1:
    print("Found it!")
else:
    print("Can't find character")

# 4)მომხმარებელს შემოატანინეთ მისი გვარი, შემდეგ შეეკითხეთ როგორ უნდა რო შეიცვალოს მისი გვარის ასოები, თუ გიპასუხებთ "upper" გადაიყვანეთ მთლიანი გვარი დიდ ასოებად, თუ გიპასუხებთ "lower" გადაიყვანეთ მთლიანი გვარი პატარა ასოებად და თუ გიპასუხებთ "capitalize" გადაიყვანეთ გვარის მხოლოდ პირველი ასო დიდ ასოდ.

surname1 = input("surname: ")
question = input("want to change surname (upper, lower, capitalize)")
if question == "upper":
    print(surname1.upper())
elif question == "lower":
    print(surname1.lower())
elif question == "capitalize":
    print(surname1.capitalize())