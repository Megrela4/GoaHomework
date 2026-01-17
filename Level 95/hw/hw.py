# თქვენით მოიძიეთ სამი 6 kyu ამოცანა და გააკეთეთ, რომელიც გაგიჭირდებათ გავარჩიოთ შემდეგი codewars-ის გაკვეთილზე

# https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python
def find_it(seq):
    for num in seq:
        if seq.count(num) % 2 !=0:
            return num
        
# https://www.codewars.com/kata/54da539698b8a2ad76000228/train/python
def is_valid_walk(walk):
    steps = 0
    x = 0
    y = 0

    for direction in walk:
        steps = steps + 1

        if direction == 'n':
            y = y + 1
        if direction == 's':
            y = y - 1
        if direction == 'e':
            x = x + 1
        if direction == 'w':
            x = x - 1

    if steps == 10 and x == 0 and y == 0:
        return True
    else:
        return False
    
# https://www.codewars.com/kata/54e6533c92449cc251001667/train/python
def unique_in_order(sequence):
    result = []
    index = 0

    for item in sequence:
        if index == 0:
            result.append(item)
            index = index + 1
        else:
            last = result[index - 1]
            if item != last:
                result.append(item)
                index = index + 1

    return result