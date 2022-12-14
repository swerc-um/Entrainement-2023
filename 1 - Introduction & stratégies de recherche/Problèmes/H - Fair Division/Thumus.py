a = [list(map(int, input().split(" "))) for _ in range(int(input()) * 2)]

for e in range(0, len(a), 2):
    c = a[e][0]
    d = a[e+1]
    e, f = d.count(1), d.count(2)
    if (c % 2 == 0):
        print("YES" if (sum(d) % 2 == 0)  else "NO")
    else:
        print("YES" if (e % 2 == 0 and f % 2 == 1 and e > 1) else "NO")
    
         
