from math import prod

def bezout(a, b):
    px, py = 1, 0
    x, y = 0, 1
    while b != 0:
        a, b, q = b, a % b, a // b
        px, py, x, y = x, y, px - q * x, py - q * y
    return a, px, py

def inv(a, n):
    gcd, inv, _ = bezout(a, n)
    if gcd != 1:
        return None
    return inv % n

def crt(a, n):
    x = 0
    p = prod(n)
    for ai, ni in zip(a, n):
        xi = p // ni
        x += ai * xi * inv(xi, ni)
    return x

mods = (23, 28, 33)
case = 1

while True:
    p, e, i, d = map(int, input().split())

    if p == e == i == d == -1:
        break

    sol = crt((p, e, i), mods) % prod(mods)

    if sol <= d:
        sol += prod(mods)

    print(
        "Case %d: the next triple peak occurs in %d days."
        % (case, sol - d)
    )
    case += 1
