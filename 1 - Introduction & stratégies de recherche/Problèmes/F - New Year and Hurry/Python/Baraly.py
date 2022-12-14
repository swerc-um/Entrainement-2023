elements = input().split(' ')
nombreProblemes = int(elements[0])
tempsTrajet = int(elements[1])

compteur = 0
tempsRestant = 240 - tempsTrajet

while tempsRestant >= (compteur + 1) * 5 and compteur < nombreProblemes:
    compteur += 1
    tempsRestant -= compteur * 5

print(compteur) 
