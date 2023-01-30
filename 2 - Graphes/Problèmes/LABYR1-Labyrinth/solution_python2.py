#! /usr/bin/env python2

T = int(raw_input())

def dfs(m, x):
    depths = [-1 for _ in xrange(len(m))]
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

for _ in xrange(T):
    C, R = map(int, raw_input().split())
    ids = {}
    m = []
    for x in xrange(R):
        for y, c in enumerate(raw_input()):
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

    print "Maximum rope length is " + str(dfs(m, dfs(m, 0)[1])[0]) + "."