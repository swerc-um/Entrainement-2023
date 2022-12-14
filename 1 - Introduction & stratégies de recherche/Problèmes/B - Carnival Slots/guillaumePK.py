
with open("balls.in") as balls_in:
    T = int(balls_in.readline())

    MUTABLE = ("/", "\\")

    for _ in range(T):
        r,c = map(int, balls_in.readline().split())
        balls = list(map(int, balls_in.readline().split()))
        grid = [balls_in.readline() for _ in range(r)]

        scores = list(map(int, balls_in.readline().split()))
        """ 
        Besoin que d'une seule dimension de prog dyn car on écrasera scores
        Mais on pourrait aussi implémenter les deux dimensions    
        """
        new_scores = list(scores)
        
        """ 
        On va partir de la ligne du bas et mettre à jour les scores en
        fonction des modifications qui nous permettent de le maximiser
        """
        for y in range(r-1, -1, -1):
            for x in range(c):
                if grid[y][x] in MUTABLE:
                    if x == 0: # Colonne de gauche
                        # Meilleur score à droite
                        if scores[x] < scores[x+1]: 
                            new_scores[x] = scores[x+1]
                        else: # Sinon on conserve
                            new_scores[x] = scores[x]
                    elif x == c-1: # Colonne de droite
                        # Meilleur score à gauche
                        if scores[x] < scores[x-1]: 
                            new_scores[x] = scores[x-1]
                        else: # Sinon on conserve
                            new_scores[x] = scores[x]
                    else: # Colonnes du milieu
                        # On conserve seulement si score meilleur
                        if scores[x] >= scores[x-1] and scores[x] >= scores[x+1]:
                            new_scores[x] = scores[x]
                        else:
                            # Si meilleur à gauche
                            if scores[x] < scores[x-1]:
                                new_scores[x] = scores[x-1]
                            # Si meilleur à droite (à noter : ce n'est pas un elif)
                            if scores[x-1] < scores[x+1]:
                                new_scores[x] = scores[x+1]
            # On écrase les scores pour pouvoir calculer le niveau suivant
            scores = list(new_scores)
            
        print(sum([scores[i]*balls[i] for i in range(c)]))
 
