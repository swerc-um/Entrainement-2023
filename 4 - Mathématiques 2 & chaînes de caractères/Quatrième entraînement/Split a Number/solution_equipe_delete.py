import sys

def checkSol(mid, l, n) :
    if n[mid] != '0': return int(n[:mid]) + int(n[mid:])

    midL = mid - 1
    midR = mid + 1
    while n[midL] == '0' : midL -= 1
    while midR < l and n[midR] == '0'  : midR += 1 

    sol1 = sys.maxsize
    sol2 = sys.maxsize

    if midR < l : 
        sol1 = int(n[:midR]) + int(n[midR:])
    if midL > 0 : 
        sol2 = int(n[:midL]) + int(n[midL:])

    return min(sol1, sol2)

l = int(input())
n = input()

mid = l // 2
if l % 2 == 1 :
    print(min(checkSol(mid, l, n), checkSol(mid+1, l, n)))
else :
    print(checkSol(mid, l, n))