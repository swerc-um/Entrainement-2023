from collections import deque
from math import inf

def find_augm_path(n, s, t, succ, caps, flow):
    queue = deque()
    queue.append(s)
    prev = [None] * n
    prev[s] = s
    val = [0]*n
    val[s] = inf
    while queue:
        u = queue.popleft()
        for v in succ[u]:
            res = caps[u][v] - flow[u][v]
            if res > 0 and prev[v] is None:
                val[v] = min(val[u], res)
                prev[v] = u
                if v == t: break
                else: queue.append(v)
    return prev, val[t]

def edmond_karps(n, s, t, succ, caps):
    flow = [[0]*n for _ in range(n)]
    while True:
        prev, val = find_augm_path(n, s, t, succ, caps, flow)
        if not val: break
        u = t
        while prev[u] != u:
            flow[prev[u]][u] += val
            flow[u][prev[u]] -= val
            u = prev[u]
    return flow, sum(flow[s])

def team_sort(team):
    dico = {}
    for t in team:
        for l in t:
            if l in dico:
                dico[l] += 1
            else:
                dico[l] = 1
    possible_teams = []
    maxi = 0
    for v in dico.values():
        if v > maxi:
            maxi = v
    for k,v in dico.items():
        if v >= maxi:
            possible_teams.append(k)
    return possible_teams

nb_teams = int(input())
teams = []
careers = set()
for i in range(nb_teams):
    team = team_sort(input().split())
    for t in team:
        careers.add(t)
    teams.append(team)
max_teams = int(input())
careers = list(careers)
nb_careers = len(careers)
n = 2 + nb_careers + nb_teams

caps = [[0]*n for _ in range(n)]
src = 0
puit = n-1
succ = [[] for _ in range(n)]
succ[src] = [i+1 for i in range(nb_teams)]
for i in range(nb_teams):
    caps[src][i+1] = 1
    for c in teams[i]:
        car = careers.index(c)
        succ[i+1].append(car+1+nb_teams)
        succ[car+1+nb_teams].append(i+1)
        caps[i+1][car+1+nb_teams] = 1
for i in range(len(careers)):
    succ[i+1+nb_teams].append(puit)
    caps[i+1+nb_teams][puit] = max_teams

print(edmond_karps(n, src, puit, succ, caps)[1])