from itertools import groupby, zip_longest
    
for _ in range(int(input())):
    ans = True
    for pattern, check in zip_longest(groupby(input()),groupby(input())):
        if None in [pattern, check]:
            ans = False
            break
        a = list(pattern[1])
        b = list(check[1])
        if pattern[0] != check[0] or len(a) > len(b):
            ans = False
            break
        
    print('YES' if ans else 'NO') 
