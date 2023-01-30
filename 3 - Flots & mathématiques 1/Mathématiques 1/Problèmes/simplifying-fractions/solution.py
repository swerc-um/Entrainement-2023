#! /usr/bin/env python3

from math import gcd

N = int(input())
for _ in range(N) :
    a, b = map(int, input().split('/'))
    g = gcd(a, b)
    print(f"{a//g} / {b//g}")