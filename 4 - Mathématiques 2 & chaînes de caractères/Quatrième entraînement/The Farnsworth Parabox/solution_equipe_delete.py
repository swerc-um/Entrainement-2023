from math import inf

def bellman_ford(n, src, arcs):
    dist = [inf] * n
    dist[src] = src
    prev = [None] * n
    prev[src] = src
    for i in range(n-1):
        relaxed = False
        for (w,u,v) in arcs:
            alt = dist[u] + w
            if dist[v] > alt:
                dist[v] = alt
                prev[v] = u
                relaxed = True
        if not relaxed: break
    for (w,u,v) in arcs:
        if dist[v] > dist[u] + w:
            return None
    return dist, prev

try:
    while True:
        N, B = map(int, input().split())
        if N == 0 and B == 0:
            break
        arcs = []
        for _ in range(B):
            u, v, poids = map(int, input().split())
            arcs.append((poids, u-1, v-1))
            arcs.append((-poids, v-1, u-1))
        res = bellman_ford(N, 0, arcs)
        if res is None:
            print("Y")
        else:
            print("N")

except EOFError:
    pass