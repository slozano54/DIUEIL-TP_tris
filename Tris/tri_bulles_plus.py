#!/usr/bin/python3
#-*- coding: utf8 -*-
"""
    ## Procédure tri à bulles optimisé

    * On compare les éléments deux à deux en parcourant tout le tableau.
    * On les échange s'il sont mal triés.
    * Si un parcours interne ne fait aucun échange c'est que le tri est fini !
"""
pass

#pour copier une variable
import copy 

# On fait les imports nécessaires selon le contexte
if __name__ == "__main__":    
    import utils as ui
else:
    import Tris.utils as ui   
    
def tri_bulles_plus(tab_source:list)->list:
    """
    Fonction de tri à bulles
    
    **Paramètres** tab_source : Une liste.<br>
    **Sorties** le tableau trié<br>
    **Préconditions** Le tableau n'est pas vide<br> 
    **Invariant** les éléments n-i à n sont triés<br>
    **Postconditions** le tableau est trié<br>
    **Exemples**
    >>> my_tab_to_sort = [5,1,2,4,3]
    [1,2,3,4,5]
    """
    pass

    # On va travailler sur une copie du tableau de manière à pouvoir faire plusieurs appels
    # de la fonction sans modifier le tableau d'origine  
    tab = copy.deepcopy(tab_source)

    # On récupère la taille du tableau dans une variable
    n = len(tab_source)

    #preconditions
    assert isinstance(tab,list),"Le parametre n'est pas une liste"
    assert n>0,"La liste est vide"

    # Pour compter les actions atomiques
    spy = 0
    # On ne trie le tableau que s'il a plus qu'un seul élément
    if n>=2 :
        # Traverser tous les éléments du tableau dans le pire cas
        # mais on s'arrete dès que le tableau est trié
        for i in range(n):
            if (ui.isSorted(tab)==True):
                break
            else :
                # INVARIANT :             
                # Les éléments n-i à n sont triés
                assert ui.isSorted(tab[n-i:n]),"Le tableau n'est pas trié de n-i à n"
                assert len(tab)==n,"Le nombre d'éléments du tableau a changé"
                spy += 1 #espion                       
                for j in range(0, n-i-1):
                    spy += 1  #espion                                      
                    # Si l'élément trouvé est plus grand que le suivant on échange les deux
                    if tab[j] > tab[j+1] :
                        ui.permuteTab_i_j(tab,j,j+1)

    #postconditions
    assert len(tab)==n,"Le nombre d'éléments du tableau a changé"                
    assert ui.isSorted(tab),"Le tableau n'est pas trié"
    # il faudrait vérifier que les éléments sont restés ceux de départ peut être avec une fonction à part ?        

    return [tab,spy]

if __name__=="__main__" :
    tab_a_trier=[6,5,4,3,2,1]
    print(tab_a_trier)
    print(tri_bulles_plus(tab_a_trier))
    print(tab_a_trier)