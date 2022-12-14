n = int(input())
bills = [1, 5, 10, 20, 100]
res = 0
for i in bills[::-1]:
    res += n // i
    n %= i
print(res) 
