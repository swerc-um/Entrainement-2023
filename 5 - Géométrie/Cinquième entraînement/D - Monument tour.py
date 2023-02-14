x,y = map(int, input().split())
n = int(input())
    
coords = {}
vals = []
    
for i in range(0,n):
    a,b = map(int, input().split())
    if a not in coords:
        coords[a] = [b,b]
    elif b < coords[a][0]:
        coords[a][0] = b
    elif b > coords[a][1]:
        coords[a][1] = b
    
vals = []
for a in coords.values():
    vals.append(a[0])
    vals.append(a[1])
    
vals.sort()
mediane = 0
if len(vals) > 0:
    mediane = vals[len(vals)//2]
    
mini = 0
for a,b in coords.values():
    if a <= mediane <= b:
        mini += abs(a-mediane)*2+abs(b-mediane)*2
    elif a > mediane:
        mini += abs(b-mediane)*2
    else:
        mini += abs(a-mediane)*2
    
print(mini+x-1)
