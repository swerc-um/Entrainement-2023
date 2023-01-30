#! /usr/bin/env python3

def bezout(a, b):
    px, py = 1, 0
    x, y = 0, 1
    while b != 0:
        a, (q, b) = b, divmod(a, b)
        px, x = x, px - q * x
        py, y = y, py - q * y
    return a, px, py

def inv(a, n):
    gcd, inv, _ = bezout(a, n)
    if gcd != 1:
        return None
    return inv % n

N = int(input())
if N % 2 != 0 or N < 2 : print(0)
else :
    N //= 2
    p = 1
    mod = (10**9)+7
    for k in range(2, N + 1) :
        p *= ((1 + N*inv(k, mod)) % mod)
        p %= mod
    print(p)