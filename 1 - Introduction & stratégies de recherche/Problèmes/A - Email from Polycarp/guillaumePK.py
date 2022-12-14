n = int(input())

for _ in range(n):
    a = input()
    b = input()
    
    i = 0
    j = 0
    yes = True
    while i < len(a):
        if j >= len(b):
            yes = False
            break
        if b[j] != a[i]:
            yes = False
            break
        if i+1 < len(a) and a[i] == a[i+1]:
            i += 1
            j += 1
            continue
        while j < len(b) and b[j] == a[i]:
            j += 1
        i += 1
    if yes and j >= len(b):
        print("YES")
    elif j < len(b) or not yes:
        print("NO") 
