from math import prod
from bezout import inv

def crt(a, n):
    x = 0
    p = prod(n)
    for ai, ni in zip(a, n):
        xi = p // ni
        x += ai * xi * inv(xi, ni)
    return x
