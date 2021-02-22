#!/usr/bin/python3
#-*- coding: utf8 -*-
"""
    Procédure tri par sélection
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
    
    `Préconditions`
    
        * Le tableau n'est pas vide 

    `Invariant`
    
        * les éléments n-i à n sont triés

    `Postconditions`
    
        * le tableau est trié
    

    `Exemples`
    
    >>> my_tab_to_sort = [5,1,2,4,3]
    [1,2,3,4,5]
    """
    pass

    return True


if __name__=="__main__" :
    tab_a_trier=[5,4,3,2,1]
    print(tab_a_trier)
    print(tri_selection(tab_a_trier))