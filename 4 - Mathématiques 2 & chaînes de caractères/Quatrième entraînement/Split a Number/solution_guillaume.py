l = int(input())

n = input()
nlist = list(map(int, n))

maxsize = l
cuts = set()

for i in range(1,l):
    if nlist[i] != 0:
        if max(i, l-i) < maxsize:
            maxsize = max(i, l-i)
            cuts = set([i])
        elif max(i, l-i) == maxsize:
            cuts.add(i)

print(min(map(lambda i: int(n[:i])+int(n[i:]), cuts)))
