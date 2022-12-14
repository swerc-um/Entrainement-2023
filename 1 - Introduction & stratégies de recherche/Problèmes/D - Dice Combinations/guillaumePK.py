l=[0]*5+[1]
for i in range(int(input())):l=l[1:]+[sum(l)%1000000007]
print(l[-1]) 
