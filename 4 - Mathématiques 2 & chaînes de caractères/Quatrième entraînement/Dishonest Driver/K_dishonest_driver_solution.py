#
# Catégorie : programmation dynamique
# 
# Problème : https://swerc.eu/2018/theme/scoreboard/public/problem_41.pdf
# Pour tester une solution : https://codeforces.com/problemset/gymProblem/102465/K
# 
# On a en entrée une chaîne u dont on veut connaître la taille de la forme compressée
# On définit f(i,j) = taille de la forme compressée de la sous chaîne u_ij = u_i...u_j-1
# Lorsque i = j+1, f(i,j) = 1
# Sinon, f(i,j) est égal au minimum entre :
# - min_{i < k < j} f(i,k) + f(k,j) 
# - f(i,k) avec u_ik (le plus petit) facteur de u_ij
# En pratique, si un facteur u_ik avec k < j existe, alors le minimum sera toujours f(i,k)
# 
# Pour trouver le facteur u_ik, l'astuce consiste à concaténer u_ij avec lui-même et à
# trouver la seconde position de u_ij dans u_ij + u_ij : cela se fait en temps linéaire
# en la taille de u_ij avec string.find (algorithme de Knuth Moris Pratt)
# 
# Au final, la complexité est de O(N^3), ce qui est suffisant pour résoudre en moins de deux
# secondes un problème avec en entrée une chaîne de caractère d'au maximum 700 caractères
#

n = int(input()) # taille du chemin
u = input() # chemin
f = [[1]*(n+1) for _ in range(n)]

# On part des sous-chaînes de taille 1 et on va jusqu'à celles de taille n
# Il est important de le faire dans cet ordre car on ré-utilise les résultats calculés pour les sous-chaînes plus petites

# Si i = j+1, f(i,j) = 1 (valeur par défaut de notre tableau f)
# Sinon :
for l in range(2,n+1):
	for i in range(0,n-l+1):
		j = i+l
		# On recherche s'il existe un facteur u_ik de u_ij avec k < j
		uij = u[i:i+l]
		# On essaie de trouver la seconde occurrence de uij dans uij_uij
		pos = (uij*2).find(uij,1)
		
		# Si un tel facteur existe, alors f(i,j) = f(i,k) et k = i+pos
		if l > pos:
			f[i][j] = f[i][i+pos]
		else:
			# Sinon on sélectionne le découpage de u_ij en deux sous-chaînes
			# ayant une compression de taille minimale
			f[i][j] = len(uij)
			
			for k in range(i+1,j):
				s = f[i][k] + f[k][j]
				if s < f[i][j]:
					f[i][j] = s

# Finalement, on affiche f(0,n) qui correspond à la compression de taille minimale de u = u_{0,n-1}
print(f[0][n])
