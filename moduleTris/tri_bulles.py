#!/usr/bin/python3
#-*- coding: utf8 -*-
"""
    Procédure tri à bulles
"""
pass


def tri_bulles(tab:list)->list:
    """Fonction de tri à bulles
    `Paramètres`

        * tab : Une liste.        

    `Sorties`

        * le tableau trié
    
    `Notes`
    
        * ...

    `Exemples`
    
    >>> my_tab_to_sort = [5,1,2,4,3]
    [1,2,3,4,5]
    """
    pass

    # On récupère la taille du tableau dans une variable
    n = len(tab)    

    #preconditions
    assert isinstance(tab,list),"Le parametre n'est pas une liste"
    assert n>0,"La liste est vide"

    # On ne trie le tableau que s'il a plus qu'un seul élément
    if n>=2 :
        # Traverser tous les éléments du tableau
        for i in range(n):
            # INVARIANT : le tableau contient toujours n éléments
            assert len(tab)==n,"Le nombre d'éléments du tableau a changé"            
            for j in range(0, n-i-1):
                # Si l'élément trouvé est plus grand que le suivant on échange les deux
                if tab[j] > tab[j+1] :
                    tab[j], tab[j+1] = tab[j+1], tab[j]

    #postconditions
    assert len(tab)==n,"Le nombre d'éléments du tableau a changé"            
    # il faudrait vérifier que les éléments sont restés ceux de départ peut être avec une fonction à part ?
    # il faudrait vérifier que le tableau est trié, peut être avec une fonction à part ?

    return tab

if __name__=="__main__" :
    tab_a_trier=[5,4,3,2,1]
    print(tab_a_trier)
    print(tri_bulles(tab_a_trier))
    
    

