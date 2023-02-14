#!/usr/bin/env python3
# swerc 2017 - christoph dürr

"""Blowing candles

solution in time O(N log N)

observation: the optimal strip is defined by two successive points from the
convex hull and one "opposite" point of convex hull.

"""

from math import sqrt

def readInt():      return int(input())
def readStr():      return input().strip()
def readInts():     return map(int, input().split())

def left_turn(a, b, c):
    return (a[0] - c[0]) * (b[1] - c[1]) - (a[1] - c[1]) * (b[0] - c[0]) > 0


def dist2(p0, p1, p2):
    """distance from point p0 to line (p1,p2)
    https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line#Line_defined_by_two_points
    """
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2
    num = ((y2 - y1)*x0 - (x2 - x1)*y0 + x2 * y1 - y2 * x1) ** 2
    denom = (y2 - y1)**2 + (x2 - x1)**2
    return num / denom


def andrew(S):
    """Convex hull by Andrew
    """
    S.sort()
    top = []
    bot = []
    for p in S:
        while len(top) >= 2 and not left_turn(p, top[-1], top[-2]):
            top.pop()
        top.append(p)
        while len(bot) >= 2 and not left_turn(bot[-2], bot[-1], p):
            bot.pop()
        bot.append(p)
    return bot[:-1] + top[:0:-1]


def solve(S):
    C = andrew(S)
    n = len(C)
    b = 1
    # small improvement : minimize calls to dist
    best = float("inf")
    for a in range(len(C)):
        d = dist2(C[b], C[a], C[a - 1])
        d1 = dist2(C[(b + 1) % n], C[a], C[a - 1])
        while d < d1:
            b = (b + 1) % n
            d = d1
            d1 = dist2(C[(b + 1) % n], C[a], C[a - 1])
        if a == 0 or d < best:
            best = d
    return sqrt(best)    # compute just once sqrt. Does not improve much (reduce by factor 0.9)


N, radius = readInts()
S = [tuple(readInts()) for _ in range(N)]
print(solve(S))
