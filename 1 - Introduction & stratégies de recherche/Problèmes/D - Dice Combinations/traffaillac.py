n = int(input())
counts = [1] * 8
for i in range(2, n+1):
	counts[i&7] = sum(counts[(i-j)&7] for j in range(1, 7) if i-j>=0) % 1000000007
print(counts[n&7])
 
