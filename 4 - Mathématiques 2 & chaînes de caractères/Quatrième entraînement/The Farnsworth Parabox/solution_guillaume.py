from math import inf
def bellman_ford(n, src, arcs):
  dist = [inf] * n
  dist[src] = src
  prev = [None] * n
  prev[src] = src
  for i in range(n - 1):
    relaxed = False
    for (w, u, v) in arcs:
      alt = dist[u] + w
      if dist[v] > alt:
        dist[v] = alt
        prev[v] = u
        relaxed = True
    if not relaxed: break
  for (w, u, v) in arcs:
    if dist[v] > dist[u] + w:
      return None
  return dist, prev

while True:
    N,B = map(int, input().split())
    if N == 0:
        break

    graph = []
    for _ in range(B):
        i, j, t = map(int, input().split())
        graph.append((t, i, j))
        graph.append((-t, j, i))
    
    negative_cycle = bellman_ford(N+1, 1, graph) == None
    if negative_cycle:
        print("Y")
    else:
        print("N")
