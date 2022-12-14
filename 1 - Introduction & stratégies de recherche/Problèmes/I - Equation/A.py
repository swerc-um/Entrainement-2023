def is_composite(n):
	c = 0;
	for i in range(1, n+1):
		if n % i == 0:
			c+=1
	if c > 2:
		return True
	return False

n = int(input())
a = 2
b = a+n

for i in range(0, 1000000001):
	if is_composite(a) and is_composite(b):
		print(b, " ", a)
		break
	a+=1;
	b+=1;
