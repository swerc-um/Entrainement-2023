from math import hypot

def dist(p,q):
    return hypot(p[0]-q[0], p[1]-q[1])

def reflect(x, p):
    return (2*x-p[0], p[1])

T = int(input())

for i in range(T):
    a,b,c,x = map(int, input().split())
    hHouse = (b,0)
    gmHouse = (0,a)
    inter = (b*(x/100), a-a*(x/100))
    gmHouseReflect = reflect(b+c, gmHouse)
    interReflect = reflect(b+c, inter)
    
    print("{:.9f}".format(dist(hHouse, gmHouseReflect) + dist(gmHouse, inter)
                          + dist(interReflect, hHouse)))
