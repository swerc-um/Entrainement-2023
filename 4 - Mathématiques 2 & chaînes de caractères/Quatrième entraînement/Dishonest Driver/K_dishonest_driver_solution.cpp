/*
 * Catégorie : programmation dynmatique
 * 
 * Problème : https://swerc.eu/2018/theme/scoreboard/public/problem_41.pdf
 * Pour tester une solution : https://codeforces.com/problemset/gymProblem/102465/K
 * 
 * On a en entrée une chaîne u dont on veut connaître la taille de la forme compressée
 * On définit f(i,j) = taille de la forme compressée de la sous chaîne u_ij = u_i...u_j-1
 * Lorsque i = j+1, f(i,j) = 1
 * Sinon, f(i,j) est égal au minimum entre :
 * - min_{i < k < j} f(i,k) + f(k,j) 
 * - f(i,k) avec u_ik (le plus petit) facteur de u_ij
 * En pratique, si un facteur u_ik avec k < j existe, alors le minimum sera toujours f(i,k)
 * 
 * Pour trouver le facteur u_ik, l'astuce consiste à concaténer u_ij avec lui-même et à
 * trouver la seconde position de u_ij dans u_ij + u_ij : cela se fait en temps linéaire
 * en la taille de u_ij avec std::string::find (algorithme de Knuth Moris Pratt)
 * 
 * Au final, la complexité est de O(N^3), ce qui est suffisant pour résoudre en moins d'une
 * seconde un problème avec en entrée une chaîne de caractère d'au maximum 700 caractères
 */

// Permet d'inclure toute la bibliothèque standard quand on utilise g++
// Ne pas utiliser en dehors des concours, cela ralentit la compilation
#include <bits/stdc++.h> 
using namespace std;

// La taille limite du chemin est fixée à 700 dans le sujet
// On crée nos variables globales de façon à ce que la mémoire soit allouée au lancement du programme :
// l'allocation de la mémoire au lancement du programme est plus rapide que de l'allocation dynamique
const int N=700; // Limite de la taille du problème
int f[N][N+1]; // On définit le tableau stockant les valeurs de f
string u(N,'\0'); // chemin fourni en entrée

int main(void)
{
    int n; // Taille réelle du chemin en entrée
    cin >> n >> u; // Récupération de l'entrée
    
    // On part des sous-chaînes de taille 1 et on va jusqu'à celles de taille n
    // Il est important de le faire dans cet ordre car on ré-utilise les résultats calculés pour les sous-chaînes plus petites
    
    for (size_t l = 1; l <= n; ++l)
    {
        // On calcule chaque f[i][j] tel que |u_ij| = l
        for (size_t i = 0; i+l <= n; ++i)
        {
            size_t j = i + l;
            // Si i = j+1, f(i,j) = 1
            if (l == 1)
            {
                f[i][j] = 1;
            }
            else 
            {
                // On recherche s'il existe un facteur u_ik de u_ij avec k < j
                string uij = u.substr(i, l);
                string uij_uij = uij + uij;
                // On essaie de trouver la seconde occurrence de uij dans uij_uij
                size_t pos = uij_uij.find(uij, 1);
                
                // Si un tel facteur existe, alors f(i,j) = f(i,k) et k = i+pos
                if (l > pos)
                {
                    f[i][j] = f[i][i+pos];
                }
                else 
                {
                    // Sinon on sélectionne le découpage de u_ij en deux sous-chaînes
                    // ayant une compression de taille minimale
                    f[i][j] = uij.size();
                    for (size_t k = i+1; k < j; ++k)
                    {
                        int sum = f[i][k] + f[k][j];
                        if (sum < f[i][j])
                        {
                            f[i][j] = sum;
                        }
                    }
                }
                
            }
        }
    }
    
    // Finalement, on affiche f(0,n) qui correspond à la compression de taille minimale de u = u_{0,n-1}
    cout << f[0][n] << endl;
    
    return 0;
} 
