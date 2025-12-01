# https://www.codewars.com/kata/51646de80fd67f442c000013
def strip_url_params(url, params_to_strip=None):
    if  params_to_strip is None:
         params_to_strip = []
    
    parts = url.split("?")
    base = parts[0]
    
    if len(parts) == 1:
        return url
    
    query = parts[1].split("&")
    result = {}
    
    for item in query:
        key, value = item.split("=")
        
        if key in params_to_strip:
            continue
            
        if key not in result:
            result[key] = value
            
    if len(result) == 0:
        return base
    
    final_query = []
    for i in result:
        final_query.append(i + "=" + result[i])
        
    return base + "?" + "&".join(final_query)


# https://www.codewars.com/kata/54bb6f887e5a80180900046b/train/python
def longest_palindrome (s):
    n = len(s)
    best = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            sub = s[i:j]
            if sub == sub[::-1]:
                best = max(best, j - i)
    return best