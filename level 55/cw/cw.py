# 1) შექმენით დიქშენერი რომელშიც შეინახავთ თქვენი საყვარელი მანქანის აღწერას ბრენდის სახელს, მოდელსა და გამოშვების წელს შემდეგ დიქშენერიდან გამოიტანეთ გასაღებები და მნიშვნელობები წყვილად შემდეგ კი ცალ-ცალკე 
dict1 = {
    "brand": "nissan",
    "model": "nissan gtr r35",
    "year": "random year"
}

for key, value in dict1.items():
    print(key, value)

for key in dict1.keys():
    print(key)

for value in dict1.values():
    print(value)


# 2)შექმენით 2 სეტი და ჯერ შეაერთეთ ერთმანეს შემდეგ გამოიტანეთ გნსხვავებები და მსგავსებები მათ შორის
set1 = {"python", "css", "html"}
set2 = {"js", "c++", "python"}
#გაერთიანებული
union_set = set1.union(set2)
print(union_set)

#განსხვავებები
difference1 = set1.difference(set2)
print(difference1)
difference2 = set2.difference(set1)
print(difference2)

#მსგავსებები
intersection = set.intersection(set2)
print(intersection)


# 3)შექმენით დიქშენერი რომლის მნიშვნელობებსაც გადაატარებთ forloop'ს და გამოიტანეთ ისინი ისინი
my_dict = {
    "name": "ნიკა",
    "age": 13,
    "city": "თბილისი"
}

for value in my_dict.values():
    print(value)


# 5)შექმენით dictionary და ცარიელი სია, შემდეგ for ციკლის მეშვოებით გადაუარეთ dictionary-ს და ჩაამატეთ მისი key და value-ბი სიაში
my_dict2 = {
    "name": "ნიკა",
    "age": 13,
    "city": "თბილისი"
}

my_list = []

for key, value in my_dict2.items():
    my_list.append((key, value))

print(my_list)

