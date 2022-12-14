n, k = map(int,input().split())
time = 4*60 - k
nb = 0
for i in range(1,n+1):
    time -= 5 * i
    if time >= 0:
        nb += 1

print(nb) 
