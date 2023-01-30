#! /usr/bin/env python3

import sys

def matrixinv(M) :
    n = len(M)
    for i in range(n) :
        M[i] += [int(i == k) for k in range(n)]
    h, k = 0, 0
    while h < n and k < n :
        i, a = 0, 0
        for j in range(h, n) :
            if abs(M[j][k]) > a : 
                i, a = j, abs(M[j][k])
        pivot = M[i][k]
        if pivot == 0 : raise ValueError()
        else :
            M[i], M[h] = M[h], M[i]
            for j in range(k, 2*n) : M[h][j] /= pivot
            for i in range(n) :
                if i == h or M[i][k] == 0 : continue 
                f = M[i][k]
                for j in range(k, 2*n) :
                    M[i][j] -= f * M[h][j]
            h += 1
            k += 1
    return [line[n:] for line in M]

with open("bujor.out", "w") as f :
    sys.stdout = f
    with open("bujor.in") as in_ :
        cases = int(in_.readline())
        for _ in range(cases) :
            N = int(in_.readline())
            M = [list(map(int, in_.readline().split())) for _ in range(N)]
            
            print('\n'.join(' '.join("{:.9f}".format(x) for x in line) for line in matrixinv(M)))