n = int(input())
    
d = {}
res = {}
    
sum_min = 0
sum_max = 0
    
for i in range(0, n):
    s, k = input().split()
    k = float(k)
    min_m = max(0, k-0.5)
    max_m = min(100, k+0.49)
    d[s] = [min_m, max_m]
    sum_min += min_m
    sum_max += max_m
    
#faisabilité
if sum_min > 100 or sum_max < 100:
    print("IMPOSSIBLE")
else:
    for e in d:
        min_m = max(d[e][0], d[e][1]-(sum_max-100))
        max_m = min(d[e][1], d[e][0]+(100-sum_min))
    
        print(e+" %.2f %.2f" % (min_m, max_m))
