# 1) https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python
def likes(names):
    count = len(names)
    if count == 0:
        return "no one likes this"
    elif count == 1:
        return f"{names[0]} likes this"
    elif count == 2:
        return f"{names[0]} and {names[1]} like this"
    elif count == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {count - 2} others like this"

# 2) https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python
def create_phone_number(n):
    part1 = f"({n[0]}{n[1]}{n[2]})"
    part2 = f" {n[3]}{n[4]}{n[5]}"
    part3 = f"-{n[6]}{n[7]}{n[8]}{n[9]}"
    return part1 + part2 + part3

# 3) https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python
def find_it(seq):
    for num in seq:
        if seq.count(num) % 2 !=0:
            return num

# 4) https://www.codewars.com/kata/5abd66a5ccfd1130b30000a9/train/python
def row_weights(array):
    team1 = sum(array[::2])
    team2 = sum(array[1::2])
    return (team1, team2)

# 5) https://www.codewars.com/kata/556196a6091a7e7f58000018/train/python
def largest_pair_sum(numbers): 
    numbers.sort()
    return numbers[-1] + numbers[-2]
