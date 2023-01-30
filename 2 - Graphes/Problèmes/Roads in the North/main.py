def find_farthest(neighbs, root, parent = None):
    result = (root, 0)

    for neighb, length in neighbs[root]:
        if neighb != parent:
            sub_result = find_farthest(neighbs, neighb, root)
            if sub_result[1] + length > result[1]:
                result = (sub_result[0], sub_result[1] + length)

    return result

end = False

while not end:
    neighbs = [[] for i in range(10_001)]

    try:
        line = input()
        while line:
            f, t, l = map(int, line.split())
            neighbs[f].append((t, l))
            neighbs[t].append((f, l))
            line = input()
    except EOFError:
        end = True

    u, _ = find_farthest(neighbs, f)
    v, dist = find_farthest(neighbs, u)

    print(dist)
