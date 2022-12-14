n = int(input())
c = 0
for b in (100, 20, 10, 5, 1):
	c += n // b
	n %= b
print(c)
 
