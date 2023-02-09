def tarjan(graph):
    """Strongly connected components by Tarjan, iterative implementation
    :param graph: directed graph in listlist format, cannot be listdict
    :returns: list of lists for each component
    :complexity: linear
    """
    n = len(graph)
    dfs_num = [None] * n
    dfs_min = [n] * n
    waiting = []
    waits = [False] * n  # invariant: waits[v] iff v in waiting
    sccp = []          # list of detected components
    dfs_time = 0
    times_seen = [-1] * n
    for start in range(n):
        if times_seen[start] == -1:                    # initiate path
            times_seen[start] = 0
            to_visit = [start]
            while to_visit:
                node = to_visit[-1]                    # top of stack
                if times_seen[node] == 0:              # start process
                    dfs_num[node] = dfs_time
                    dfs_min[node] = dfs_time
                    dfs_time += 1
                    waiting.append(node)
                    waits[node] = True
                children = graph[node]
                if times_seen[node] == len(children):  # end of process
                    to_visit.pop()                     # remove from stack
                    dfs_min[node] = dfs_num[node]      # compute dfs_min
                    for child in children:
                        if waits[child] and dfs_min[child] < dfs_min[node]:
                            dfs_min[node] = dfs_min[child]
                    if dfs_min[node] == dfs_num[node]:  # representative
                        component = []                 # make component
                        while True:                    # add nodes
                            u = waiting.pop()
                            waits[u] = False
                            component.append(u)
                            if u == node:              # until repr.
                                break
                        sccp.append(component)
                else:
                    child = children[times_seen[node]]
                    times_seen[node] += 1
                    if times_seen[child] == -1:        # not visited yet
                        times_seen[child] = 0
                        to_visit.append(child)
    return sccp

def _vertex(lit):  # integer encoding of a litteral
    if lit > 0:
        return 2 * (lit - 1)
    return 2 * (-lit - 1) + 1

def two_sat(formula):
    """Solving a 2-SAT boolean formula
    :param formula: list of clauses, a clause is pair of literals
                    over X1,...,Xn for some n.
                    a literal is an integer, for example -1 = not X1, 3 = X3
    :returns: table with boolean assignment satisfying the formula or None
    :complexity: linear
    """
    # num_variables is the number of variables
    num_variables = max(abs(clause[p])
                        for p in (0, 1) for clause in formula)
    graph = [[] for node in range(2 * num_variables)]
    for x_idx, y_idx in formula:                           # x_idx or y_idx
        graph[_vertex(-x_idx)].append(_vertex(y_idx))     # -x_idx => y_idx
        graph[_vertex(-y_idx)].append(_vertex(x_idx))     # -y_idx => x_idx
    sccp = tarjan(graph)
    comp_id = [None] * (2 * num_variables)  # each node's component ID
    assignment = [None] * (2 * num_variables)
    for component in sccp:
        rep = min(component)             # representative of the component
        for vtx in component:
            comp_id[vtx] = rep
            if assignment[vtx] is None:
                assignment[vtx] = True
                assignment[vtx ^ 1] = False    # complementary literal
    for i in range(num_variables):
        if comp_id[2 * i] == comp_id[2 * i + 1]:
            return None                        # insatisfiable formula
    return assignment[::2]

while True:
    C, P = map(int, input().split())
    
    if C == 0 and P == 0:
        break
    
    clauses = [None]*(C*2+1)
    clauses[-1] = (P+1, P+1)
    
    for i in range(C):
        X, Y, S, T = map(lambda x: x if x else -(P+1), map(int, input().split()))
        if (X, Y) != (-(P+1), -(P+1)):
            clauses[2*i] = (X, Y)
        else:
            clauses[2*i] = (P+1, P+1)
        if (S, T) != (-(P+1), -(P+1)):
            clauses[2*i+1] = tuple(map(lambda x: -x if x != -(P+1) else x, (S, T)))
        else:
            clauses[2*i+1] = (P+1, P+1)
    
    if not two_sat(clauses):
        print("no")
    else:
        print("yes")
