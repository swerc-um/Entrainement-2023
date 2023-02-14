from math import hypot
from random import shuffle

def dist(p,q):
    return hypot(p[0]-q[0], p[1]-q[1])

def cell(point, size):
    x,y = point
    return (int(x // size), int(y // size))

def improve(S, d):
    G = {}
    for p in S:
        a,b = cell(p, d/2)
        for a1 in range(a - 2, a + 3):
            for b1 in range(b - 2, b + 3):
                if (a1, b1) in G:
                    q = G[a1, b1]
                    pq = dist(p, q)
                    if pq < d:
                        return pq, p, q
        G[a,b] = p
    return None

def closest_points(S):
    shuffle(S)
    assert len(S) >= 2
    p, q = S[0], S[1]
    d = dist(p, q)
    while d > 0:
        r = improve(S, d)
        if r:
            d, p, q = r
        else:
            break
    return p, q

n = int(input())
pts = []
for _ in range(n):
    inp = input()
    a, b = map(int, inp.split())
    pts.append((a,b))

ptSave = pts[::]

p,q = closest_points(pts)
a = ptSave.index(p)
b = ptSave.index(q)
if b < a:
    a, b = b, a
d = dist(p,q)
print(a,b,"{:.6f}".format(d)) 
