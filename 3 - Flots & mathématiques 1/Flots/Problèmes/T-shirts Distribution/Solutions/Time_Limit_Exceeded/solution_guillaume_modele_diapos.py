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

S,M,L,XL,XXL,XXXL = map(int, input().split())
N = int(input())

participants = [None]*N
succ = defaultdict(list, {"source": ["S", "M", "L", "XL", "XXL", "XXXL"]})
caps = defaultdict(dict, {"source": {"S": S, "M": M, "L": L, "XL": XL, "XXL": XXL, "XXXL": XXXL}})

for i in range(N):
    sizes = (input(),)
    if "," in sizes[0]:
        sizes = tuple(sizes[0].split(","))
    for size in sizes:
        succ[size].append(i)
        caps[size][i] = 1
    succ[i].append("target")
    caps[i]["target"] = 1

for u in succ:
    for v in succ:
        if u not in succ[v]:
            succ[v].append(u)
            caps[v][u] = 0

flow, maxflow = edmonds_karp("source", "target", succ, caps)

if maxflow < N:
    print("NO")
    exit()

for size in succ["source"]:
    for i in succ[size]:
        if type(i) is int and flow[size][i]:
            participants[i] = size

print("YES")
for p in participants:
    print(p)
