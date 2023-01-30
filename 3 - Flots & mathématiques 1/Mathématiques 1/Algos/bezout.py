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
