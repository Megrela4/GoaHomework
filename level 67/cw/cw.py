# 1) https://www.codewars.com/kata/5672a98bdbdd995fad00000f/train/python
def rps(p1, p2):
    if p1 == "scissors" and p2 == "paper":
        return "Player 1 won!"
    elif p1 == "scissors" and p2 == "rock":
        return "Player 2 won!"
    elif p1 == "rock" and p2 == "scissors":
        return "Player 1 won!"
    elif p1 == "paper" and p2 == "scissors":
        return "Player 2 won!"
    elif p1 == "rock" and p2 == "paper":
        return "Player 2 won!"
    elif p1 == "paper" and p2 == "rock":
        return "Player 1 won!"
    else:
        return "Draw!"
    
# 2) https://www.codewars.com/kata/5ce9c1000bab0b001134f5af/train/python
def quarter_of(month):
    return (month - 1) // 3 + 1

# 3) https://www.codewars.com/kata/56efc695740d30f963000557/train/python
def to_alternating_case(string):
    result = ''
    for i in string:
        if i.isupper():
            result += i.lower()
        else:
            result += i.upper()
    return result
# 4) https://www.codewars.com/kata/563b662a59afc2b5120000c6/train/python
def nb_year(p0, percent, aug, p):
    years = 0
    while p0 < p:
        p0 += int(p0 * percent / 100) + aug
        years += 1
    return years

# 5) https://www.codewars.com/kata/56f69d9f9400f508fb000ba7/train/python
def monkey_count(n):
    result = []
    for i in range(1, n + 1):
        result.append(i)
    return result

# 6) https://www.codewars.com/kata/542c0f198e077084c0000c2e/train/python
def divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count