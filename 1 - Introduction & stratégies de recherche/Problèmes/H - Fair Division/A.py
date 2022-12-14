def subset_sum(b, n, s):
	table = [[False]*(s+1)]*(n+1)
	
	# si la somme vaut 0 alors vrai 
	for i in range(n+1):
		table[i][0] = True
	# si la somme attendue n'est pas 0 mais que le set est vide : false
	for i in range(1, s+1):
		table[0][i] = False

	# DP : remplir la table
	for i in range(1, n+1):
		for j in range(1, s+1):
			if j < b[i-1]:
				table[i][j] = table[i-1][j]
			if j >= b[i-1]:
				table[i][j] = (table[i-1][j] or table[i-1][j-b[i-1]])

	return table[n][s]
	
	

t = int(input())

for i in range(t):
	
	s=0
	n = int(input())
	
	b = list(map(int, input().split()))
	s = sum(b)
	if s%2==0 and subset_sum(b, n, int(s/2)):
		print("YES")
	else:
		print("NO")
