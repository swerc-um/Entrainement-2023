a = [input() for e in range(int(input()) * 2)]

for i in range(0, len(a), 2):
    m, p = a[i], a[i+1]
    b = 0
    j = b
    n = "YES"
    if (len(m) > len(p)):
        print("NO")
    else:
        for e in p:
            if len(m) > b and e == m[b]:
                j = b
                b+=1
            elif e == m[j]:
                pass
            else:
                n = "NO"
                break
        if (b < len(m)):
            n = "NO"
        print(n) 
