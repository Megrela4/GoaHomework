# 1) შექმენით dictionary სადაც შეინახავთ მინიმუმ 3 key'ს და ასევე შექმენით 2 ცარიელი სია for loop'ის დახმარებით პირველ სიაში დაამატეთ key ხოლო მეორე სიაში კი value ბოლოს კი გამოიტანეთ ერთად. 
dict1 = {
    "name": "nikoloz",
    "last_name": "megrelishvili",
    "age": "13"
}
keys = []
values = []

for key in dict1.keys():
    keys.append((key))
print(keys)

for value in dict1.values():
    values.append(value)
print(values)


# 2) მოცემული გაქვთ რაიმე result ცვლადი რომელშიც შეყვანილია სია [10,43,12,11,94,10,55,7,11] თქვენი დავალებაა გააქროთ ყველა დუბლიკატი ლისტიდან „თანმიმდევრობას მნიშვნელობა არაქვს“.
result = [10,43,12,11,94,10,55,7,11]
result = list(set(result))
print(result)


# 5) შექმენით სეტის მსგავსი ფუნქცია რომელიც მიიღებს ლისტს და ლისტიდან წაშლის დუბლიკატებს „ფუნქციაში არ გამოიყენოთ სეტი“
def remove_duplicates(lst):
    unique_list = []
    
    for item in lst:
        if item not in unique_list:  
            unique_list.append(item)
    return unique_list
