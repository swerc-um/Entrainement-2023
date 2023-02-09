from collections import deque, defaultdict
from math import inf
def find_augm_path(n, s, t, succ, caps, flow):
  queue = deque()
  queue.append(s)
  prev = [None] * n
  prev[s] = s
  val = [0] * n
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
def edmonds_karp(n, s, t, succ, caps):
  flow = [[0] * n for i in range(n)]
  while True:
    prev, val = find_augm_path(
      n, s, t, succ, caps, flow)
    if not val: break
    u = t
    while prev[u] != u:
      flow[prev[u]][u] += val
      flow[u][prev[u]] -= val
      u = prev[u]
  return flow, sum(flow[s])

n = int(input())
capital_letters = tuple(chr(i+ord("A")) for i in range(26))
node = {"source": 0, "target": 1}
node.update({capital_letters[i]: i+2 for i in range(26)})
defaultedges = tuple((node[capital_letters[i]], node["target"]) for i in range(26))
succ = defaultdict(list, {X: [Y] for X, Y in defaultedges})
caps = defaultdict(lambda: defaultdict(lambda: 0))
tn = len(node)

for _ in range(n):
    team = input().split()
    
    count = [0]*26
    for p in team:
        for c in p:
            count[ord(c)-ord("A")] += 1
    
    m = max(count)
    careers = set(filter(lambda x: count[ord(x)-ord("A")] == m, capital_letters))
    
    succ[node["source"]].append(tn)
    caps[node["source"]][tn] = 1
    
    for career in careers:
        succ[tn].append(node[career])
        caps[tn][node[career]] = 1
    
    tn += 1

k = int(input())
caps.update({X: defaultdict(lambda: 0, {Y: k}) for X, Y in defaultedges})

for i in set(succ.keys()):
    for j in succ[i]:
        succ[j].append(i)
        
flow, max_flow = edmonds_karp(tn, node["source"], node["target"], succ, caps)

print(max_flow)
