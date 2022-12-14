n = int(input())

bills = {}
bills[100]= 0
bills[20]= 0
bills[10] = 0
bills[5] = 0
bills[1] = 0

for k in bills.keys():
	
	bills[k] = int(n/k)
	n-=bills[k]*k
	
print(sum(bills.values()))


