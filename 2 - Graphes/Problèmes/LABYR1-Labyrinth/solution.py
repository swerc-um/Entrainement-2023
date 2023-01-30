#! /usr/bin/env python3

from time import time

###############################################################################
# GREEDY 
###############################################################################

def dfs(m, x):
    depths = [-1 for _ in range(len(m))]
    depths[x] = 0
    stack = [x]

    while len(stack):
        x = stack.pop(0)
        for v in m[x]:
            if depths[v] == -1:
                depths[v] = depths[x] + 1
                stack.append(v)
    
    m = max(depths)
    return (m, depths.index(m))

###############################################################################
# DYNAMIC
###############################################################################
def dynamic(graph) :
    b, t = [None] * len(graph), [None] * len(graph)
    parents = [None]
    u = 0
    while u is not None :
        found = False
        for v in graph[u] :
            if v != parents[-1] and (b[v] is None or t[v] is None) :
                parents.append(u)
                u = v 
                found = True
                break
        if not found :
            if u != 0 and len(graph[u]) == 1 :
                t[u] = b[u] = 0
            else :
                b[u] = 1 + max(b[v] for v in graph[u] if v != parents[-1]) 

                mtu = max(t[v] for v in graph[u] if v != parents[-1])
                max_enfants = b[u]
                for u1 in graph[u] :
                    for u2 in graph[u] :
                        if u1 == parents[-1] or u2 == parents[-1] or u1 >= u2 :
                            continue 

                        nmax = b[u1] + 2 + b[u2]
                        if nmax > max_enfants : max_enfants = nmax
                t[u] = max(mtu, max_enfants)
            u = parents.pop()

    return t[0]

T = int(input())

for _ in range(T):
    C, R = map(int, input().split())
    ids = {}
    m = []
    for x in range(R):
        for y, c in enumerate(input()):
            if c == '.':
                new_id = len(m)
                m.append([])
                ids[(x, y)] = new_id

                if x != 0 and (x - 1, y) in ids:
                    left_id = ids[(x - 1, y)]
                    m[new_id].append(left_id)
                    m[left_id].append(new_id)
                if y != 0 and (x, y - 1) in ids:
                    top_id = ids[(x, y - 1)]
                    m[new_id].append(top_id)
                    m[top_id].append(new_id)

    if len(m) <= 1 : print("Maximum rope length is 0.")
    else : 
        st = time()
        print(f"Maximum rope length is {dynamic(m)}. Time : {time() - st}s")
        st = time()
        print(f"Maximum rope length is {dfs(m, dfs(m, 0)[1])[0]}. Time : {time() - st}s")