richesse = int(input())

typesMonnaie = [100, 20, 10, 5, 1]

compteur = 0

while richesse > 0:
    if richesse >= typesMonnaie[0]:
        richesse -= typesMonnaie[0]
    elif richesse >= typesMonnaie[1]:
        richesse -= typesMonnaie[1]
    elif richesse >= typesMonnaie[2]:
        richesse -= typesMonnaie[2]
    elif richesse >= typesMonnaie[3]:
        richesse -= typesMonnaie[3]
    elif richesse >= typesMonnaie[4]:
        richesse -= typesMonnaie[4]
    compteur += 1
    
print(compteur) 
