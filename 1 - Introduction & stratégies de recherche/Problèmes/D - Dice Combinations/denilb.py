n = int(input())
D = [0] * (n+1)
D[0] = 1
for i in range(1,n+1):
    for k in range(1, min(i, 6) + 1):
        D[i] += D[i - k]
        D[i] %= 1000000007
print(D[n]) 
