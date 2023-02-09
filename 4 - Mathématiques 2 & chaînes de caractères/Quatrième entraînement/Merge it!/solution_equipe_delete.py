def diviseurs(n, l):
    div = [0,0,0]

    for i in range(n):
        div[l[i]%3] += 1

    diff = min(div[1],div[2])
    div[0] += diff
    div[1] -= diff
    div[2] -= diff

    return div[0] + (div[1]//3) + (div[2]//3)

t = int(input())
for _ in range(t):
    n = int(input())
    entiers = [int(a)for a in input().split()]
    print(diviseurs(n, entiers))


# code golf (le même en plus court)

for _ in range(int(input())):
    input()
    liste = [int(a)%3 for a in input().split()]
    div = [liste.count(k) for k in range(3)]
    diff = min(div[1], div[2])
    print(div[0]+diff + (div[1]-diff)//3 + (div[2]-diff)//3)