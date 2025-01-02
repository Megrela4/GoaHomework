# 1)https://www.codewars.com/kata/53ee5429ba190077850011d4
def double_integer(i):
    return i * 2
# 2)https://www.codewars.com/kata/55b42574ff091733d900002f

# 3)https://www.codewars.com/kata/57f780909f7e8e3183000078
def grow(arr):
    result = 1
    for i in arr:
        result *= i
    return result
# 4)https://www.codewars.com/kata/57a2013acf1fa5bfc4000921/train/python

# 5)https://www.codewars.com/kata/55f73be6e12baaa5900000d4
def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague
# 6)https://www.codewars.com/kata/56b1f01c247c01db92000076
def double_char(s):
    result = ""
    for i in s:
        result += i * 2
    return result
# 7)https://www.codewars.com/kata/51f2b4448cadf20ed0000386

# 8)https://www.codewars.com/kata/59a8570b570190d313000037

# 1)შექმენით სია, სადაც გექნებათ 5 ელემენტი. წაშალეთ სიის მე-3 ელემენტი და დაამატეთ ახალი მე-0 ინდექსზე. საბოლოოდ დააბრუნეთ ეს სია
list = [1, 2, 3, 4]
list.pop(2)
list.insert(0, 5)
print(list)

# 2)შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა ორი რიცხვი შემდეგ ,პირველი რიცხვი აიყვანეთ მეორე რიცხვის ხარისხში და დააბრუნეთ
# ?

# 3)შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა სია შემდეგ უნდა შეამოწმოთ ამ სიის სიგრძე თუ ლუწია დააბრუნეთ --> List length is even, ხოლო სხვა შემთხვევაში დააბრუნეთ --> List length is odd
def even_odd(list):
    if len(list) % 2 == 0:
        return "List length is even"
    else:
        return "List length is odd"
    


