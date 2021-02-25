#!/usr/bin/python3
#-*- coding: utf8 -*-
"""
    ## Procédure tri à bulles optimisé

    * On compare les éléments deux à deux en parcourant tout le tableau.
    * On les échange s'il sont mal triés.
    * Si un parcours interne ne fait aucun échange c'est que le tri est fini !
"""
pass

# On fait les imports nécessaires selon le contexte
if __name__ == "__main__":    
    import utils as ui
    from config import *
else:
    import Tris.utils as ui   
    from Tris.config import *  

    
def tri_bulles_plus(tab:list)->list:
    """
    Fonction de tri à bulles
    
    **Paramètres** tab : Une liste.<br>
    **Sorties** le tableau trié<br>
    **Préconditions** Le tableau n'est pas vide<br> 
    **Invariant** les éléments n-i à n sont triés<br>
    **Postconditions** le tableau est trié<br>
    **Exemples**
    >>> my_tab_to_sort = [5,1,2,4,3]
    [1,2,3,4,5]
    """
    pass

    # On récupère la taille du tableau dans une variable
    n = len(tab)

    #preconditions
    assert isinstance(tab,list),"Le parametre n'est pas une liste"
    assert n>0,"La liste est vide"
    #espion
    global spy
    spy = 0
    my_ext_spy = 0    
    # On ne trie le tableau que s'il a plus qu'un seul élément
    if n>=2 :
        # Traverser tous les éléments du tableau dans le pire cas
        # mais on s'arrete dès que le tableau est trié
        i=0
        #while (i<n and (ui.isSorted(tab)==False)):        
        for i in range(n):
            #print('1e spy tribullesplus : ',spy)
            my_ext_spy = spy
            if (ui.isSorted(tab)==True):
                break
            else :
                # INVARIANT :             
                # Les éléments n-i à n sont triés
                #print("i=",i," : ",tab)
                assert ui.isSorted(tab[n-i:n]),"Le tableau n'est pas trié de n-i à n"
                assert len(tab)==n,"Le nombre d'éléments du tableau a changé"
                #print("tri bulles plus")
                spy += 1 #espion           
                for j in range(0, n-i-1):
                    spy += 1  #espion                          
                    # Si l'élément trouvé est plus grand que le suivant on échange les deux
                    if tab[j] > tab[j+1] :
                        #tab[j], tab[j+1] = tab[j+1], tab[j]
                        ui.permuteTab_i_j(tab,j,j+1)
                #print('2e spy tribullesplus : ',spy)
                #my_ext_spy = spy
            i+=1

    #postconditions
    assert len(tab)==n,"Le nombre d'éléments du tableau a changé"                
    assert ui.isSorted(tab),"Le tableau n'est pas trié"
    # il faudrait vérifier que les éléments sont restés ceux de départ peut être avec une fonction à part ?        

    return [tab,spy]
    #return [tab,sum_spy]
    #return [tab,my_ext_spy]

if __name__=="__main__" :
    tab_a_trier=[5,4,3,2,1]
    print(tab_a_trier)
    print(tri_bulles_plus(tab_a_trier))