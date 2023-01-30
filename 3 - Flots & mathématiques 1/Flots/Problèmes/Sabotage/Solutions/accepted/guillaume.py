from collections import deque
from math import inf
from collections import defaultdict

def find_augm_path(s, t, succ, caps, flow):
  queue = deque()
  queue.append(s)
  prev = defaultdict(lambda:None)
  prev[s] = s
  val = defaultdict(lambda:0)
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

def edmonds_karp(s, t, succ, caps):
  flow = defaultdict(lambda: defaultdict(lambda: 0))
  while True:
    prev, val = find_augm_path(s, t, succ, caps, flow)
    if not val: break
    u = t
    while prev[u] != u:
      flow[prev[u]][u] += val
      flow[u][prev[u]] -= val
      u = prev[u]
  return flow, sum(flow[s].values()) 

while True:
    N,M = map(int, input().split())
    if N == 0 and M == 0: 
        break
    
    succ = defaultdict(list)
    caps = defaultdict(dict)
    source = 1
    target = 2
    
    for _ in range(M):
        u, v, c = map(int, input().split())
        if u != target and v != source:
            succ[u].append(v)
            caps[u][v] = c
        if u != source and v != target:
            succ[v].append(u)
            caps[v][u] = c
    
    flow, max_flow = edmonds_karp(source, target, succ, caps)
    
    reachable_vertices = set([source])
    to_explore = [source]
    seen = set()
    
    while to_explore:
        v = to_explore.pop()
        if v not in seen:
            seen.add(v)
            for n in succ[v]:
                if n not in seen and caps[v][n] > flow[v][n]:
                    reachable_vertices.add(n)
                    to_explore.append(n)
                    
    for v in reachable_vertices:
        for n in succ[v]:
            if n not in reachable_vertices:
               print(v, n)
    
    print()
