n = int(input())

def countDynamique(n):
    listeElement = [1] + [2**(i-1) for i in range(1,7)]

    for _ in range(6,n):
        listeElement.append(sum([listeElement[-j] for j in range(1, 7)]) % (10**9 + 7))

    return listeElement[n]

print(countDynamique(n)) 
