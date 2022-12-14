a = int(input())
b = [100, 20, 10, 5, 1]
c = 0
while a != 0 or len(b) > 0:
    if b[0] > a:
        b.pop(0)
    else:
        a -= b[0]
        c += 1
print(c) 
