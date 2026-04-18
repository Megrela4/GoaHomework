# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272
def high(x):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    sityvebi = x.split()
    sityva = ""
    highest_score = 0
    
    for i in sityvebi:
        score = 0
        for aso in i:
            score += alphabet.index(aso) + 1
        
        if score > highest_score:
            highest_score = score
            sityva = i
            
    return sityva

# https://www.codewars.com/kata/5420fc9bb5b2c7fd57000004
def highest_rank(arr):
    best_num = arr[0]
    best_count = 0
    
    for num in arr:
        count = arr.count(num)
        
        if count > best_count or (count == best_count and num > best_num):
            best_count = count 
            best_num = num
            
    return best_num
