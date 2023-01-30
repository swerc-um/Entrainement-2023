from heapq import *
import math

def var_dij (r, t, neighbors, B):
    q = [(0,0,r)]
    distances = {r: {0: 0}}
    seen = set()
    
    while q:
        cost,dist,node = heappop(q)
        if (node, dist) in seen: continue
        seen.add((node, dist))
        if node == t: 
            return cost
        
        for n in neighbors[node]:
            costn,distn,noden = n
            if (noden, distn) in seen: continue
            newdist = dist + distn
            newcost = cost + costn
            if newdist > B: continue
            if noden not in distances: distances[noden] = {}
            if newdist not in distances[noden] or distances[noden][newdist] > newcost:
                distances[noden][newdist] = newcost 
                heappush(q, (newcost, newdist, noden))
    return -1

def edist (n1, n2):
    return math.ceil(math.hypot(n1[0]-n2[0], n1[1]-n2[1]))

# Récupération de la complexe entrée...
xs,ys = map(int, input().split())
xd,yd = map(int, input().split())
B = int(input())
costs = []
costs.append(int(input()))
T = int(input())
for _ in range(1,T+1):
    costs.append(int(input()))
N = int(input())
nodes = []
adj = {}
for i in range(0,N):
    x,y,l,*tab = map(int, input().split())
    nodes.append((x,y))
    for j in range(l):
        if i not in adj: adj[i] = set()
        if tab[j*2] not in adj: adj[tab[j*2]] = set()
        adj[i].add((tab[j*2], tab[j*2+1]))
        adj[tab[j*2]].add((i, tab[j*2+1]))
nodes.append((xs,ys))
nodes.append((xd,yd))

# Construction de la matrice des distances
distances = [[0]*(N+2) for _ in range(N+2)] 
for i in range(N+2):
    for j in range(N+2):
        distances[i][j] = edist(nodes[i], nodes[j])
        
neighbors = [[] for _ in range(N+2)]

for i in adj:
    for e in adj[i]:
        neighbors[i].append((costs[e[1]]*distances[i][e[0]], distances[i][e[0]], e[0]))
        
for i in range(N+2):
    neighbors[N].append((costs[0]*distances[i][N], distances[i][N], i))
    neighbors[i].append((costs[0]*distances[i][N], distances[i][N], N))
    neighbors[N+1].append((costs[0]*distances[i][N+1], distances[i][N+1], i))
    neighbors[i].append((costs[0]*distances[i][N+1], distances[i][N+1], N+1))

print(var_dij(N, N+1, neighbors, B))
