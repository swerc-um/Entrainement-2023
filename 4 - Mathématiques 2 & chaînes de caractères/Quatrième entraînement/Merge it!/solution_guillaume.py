T = int(input())
for _ in range(T):
    n = input()
    Z,U,D = 0,0,0
    numbers = map(lambda x: x%3, map(int, input().split()))
    for m in numbers:
        if m == 0:
            Z += 1
        elif m == 1:
            U += 1
        else:
            D += 1
    if U < D:
        print(Z+U+(D-U)//3)
    else:
        print(Z+D+(U-D)//3)
        
