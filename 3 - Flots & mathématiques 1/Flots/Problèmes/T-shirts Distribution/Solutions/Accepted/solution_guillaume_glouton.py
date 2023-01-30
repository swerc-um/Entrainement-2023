S,M,L,XL,XXL,XXXL = map(int, input().split())
N = int(input())

counts = {"S": S, "M": M, "L": L, "XL": XL, "XXL": XXL, "XXXL": XXXL}
couples = [("S", "M"), ("M", "L"), ("L", "XL"), ("XL", "XXL"), ("XXL", "XXXL")] 
participants = [None]*N 
groups = dict()

for i in range(N):
    sizes = input()
    if "," in sizes:
        sizes = tuple(sizes.split(","))
        if sizes not in groups:
            groups[sizes] = []
        groups[sizes].append(i)
    else:
        participants[i] = sizes
        counts[sizes] -= 1
        if counts[sizes] < 0:
            print("NO")
            exit()

for k in couples:
    if k not in groups: continue
    v = groups[k]
    for i in v:
        if counts[k[0]] > 0:
            participants[i] = k[0]
            counts[k[0]]  -= 1
        elif counts[k[1]] > 0:
            participants[i] = k[1]
            counts[k[1]]  -= 1
        else:
            print("NO")
            exit()

print("YES")
for p in participants:
    print(p)
