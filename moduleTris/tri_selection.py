#!/usr/bin/python3
#-*- coding: utf8 -*-
"""
    ## Procédure tri par sélection

    * On recherche le plus petit élément et on l'échange avec l'élément d'indice 0 du tableau
    * On recherche le plus petit élément du tableau restant et on l'échange avec l'élement d'indice 1 du tableau
    * etc jusqu'à ce que le tableau soit trié
"""
pass

# On fait les imports nécessaires selon le contexte
if __name__ == "__main__":    
    import utils as ui    
else:
    import moduleTris.utils as ui     
    
def tri_selection(tab:list)->list:
    """Fonction de tri par selection
    `Paramètres`

        * tab : Une liste.        

    `Sorties`

        * le tableau trié    

    `Exemples`
    
    >>> my_tab_to_sort = [5,1,2,4,3]
    [1,2,3,4,5]
    """
    pass

    # Taille du tableau
    n = len(tab)

    # On ne trie le tableau que s'il a plus qu'un seul élément
    if n>=2 :
        # intialiser le compteur de boucle
        i=0
        while (i<=n-2):
            
            # indice du plus petit élement restant
            i_min = i
            # initialiser le compteur de boucle pour les éléments du tableau restant
            j=i+1
            while (j<=n-1):
                # si on trouve un plus petit élément on modifie l'indice i_min
                if tab[j] < tab[i_min]:
                    i_min = j
                # incrémenter le compteur boucle secondaire
                j+=1
            # si on a modifié i_min on échange les éléments
            if (i_min != i):
                ui.permuteTab_i_j(tab,i,i_min)
            # incrémenter le compteur boucle principale
            i+=1
    
    # on retourne le tableau trié
    return tab    


if __name__=="__main__" :
    tab_a_trier=[5,4,3,2,1]
    print(tab_a_trier)
    print(tri_selection(tab_a_trier))