a, b = map(int, input().split())
c = 240 - b 
d = True
for i in range(1, a+1):
    if c - (i*5) < 0:
        print(i-1)
        d = False
        break
    else:
        c -= (i*5)
if d:
    print(a) 
