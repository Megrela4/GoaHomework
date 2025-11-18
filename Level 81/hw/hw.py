# https://www.codewars.com/kata/54bb6f887e5a80180900046b
def longest_palindrome (s):
    n = len(s)
    best = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            sub = s[i:j]
            if sub == sub[::-1]:
                best = max(best, j - i)
    return best