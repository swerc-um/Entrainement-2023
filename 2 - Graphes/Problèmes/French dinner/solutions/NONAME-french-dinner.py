#! /usr/bin/env python3

from math import inf

def bellman_ford(n, src, arcs) :
    dist = [inf] * n
    dist[src] = 0 
    prev = [None] * n 
    prev[src] = src 
    for _ in range(n - 1) :
        relaxed = False 
        for (w, u, v) in arcs :
            alt = dist[u] + w
            if dist[v] > alt :
                dist[v] = alt 
                prev[v] = u 
                relaxed = True 
        if not relaxed : break 
    for (w, u, v) in arcs :
        if dist[v] > dist[u] + w :
            return None 
    return dist, prev

# Récupération de l'entrée
N, K = map(int, input().split())
points = ['NIL']
edges = []

for _ in range(N) :
    pred, u_name, v_name, w = input().split()
    w = int(w)
    u, v = -1, -1

    try :
        u = points.index(u_name)
    except ValueError :
        points.append(u_name)
        u = len(points) - 1
        edges.append((0, 0, u))
    try :
        v = points.index(v_name)
    except ValueError :
        points.append(v_name)
        v = len(points) - 1
        edges.append((0, 0, v))

    if pred == 'BEF' :
        # B - A >= w => A - B <= -w
        edges.append((-w, v, u))
    if pred == 'SIM' :
        # |A - B| <= w donc soit A - B <= w 
        edges.append((w, v, u))
        # soit B - A <= w
        edges.append((w, u, v))

# Bellman-Ford, s'il y a un cycle négatif, c'est mort..
res = bellman_ford(len(points), 0, edges)
if res is None : 
    print("NO")
else :
    # Le plus court chemin est forcément négatif, on inverse donc le minimum des distances.
    if -min(res[0]) <= K :
        print("YES")
    else :
        print("NO")