from math import gcd, hypot
n = int(input())
points= []
for i in range(n):
    x,y= map(int,input().split())
    points.append((x,y))
surface=0
for i in range(n):
    surface+=points[i][0]*points[(i+1)%n][1]-points[(i+1)%n][0]*points[i][1]
surface = abs(surface/2)
#calcule du nombre des pts
numberOfpoint =0
for i in range(n):
    x=abs(points[i][0]-points[(i+1)%n][0])
    y=abs(points[i][1]-points[(i+1)%n][1])
    if (x == 0):
        numberOfpoint += y
    elif (y ==0):
        numberOfpoint+=x
    else:
        numberOfpoint +=gcd(x,y)
#supprimer les doublant 
numberOfpoint= int(surface- numberOfpoint/2 +1)    

print (numberOfpoint) 
