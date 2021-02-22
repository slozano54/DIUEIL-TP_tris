#!/usr/bin/python3
#-*- coding: utf8 -*-
"""
    Procédure tri à bulles
"""
pass

import copy

def isSorted(tab:list)->bool:
    """Fonction booléenne qui retourne True si le tableau passé en paramètre est trié"""
    #Le booléen de sorite
    isTrue = True    
    #La longueur du tableau
    n=len(tab)
    
    #Preconditions    
    assert isinstance(tab,list),"le paramètre n'est pas une liste"

    #initialisation du compteur de boucle
    i=0
    while i<n-1:
        #Invariant  : le ième élément est inférieur au (i+1)ème
        if tab[i]>tab[i+1]:
            isTrue = False
        i+=1
    
    #Postconditions
    assert isTrue==True,"Le tableau n'est pas trié"

    return isTrue

def permuteTab_i_j(tab:list,i:int,j:int)->list:
    """Fonction qui permute les éléments i et j d'un tableau passé en paramètre"""
    #La longueur du tableau
    n=len(tab)

    #Preconditions
    assert n>0,"Le tableau est vide"
    assert i in range(n),"i n'est pas un indice du tableau"
    assert j in range(n),"j n'est pas un indice du tableau"

    #variable tampon
    temp = tab[i]
    tab[i] = tab[j]
    tab[j]= temp

    #Postconditions
    assert len(tab)==n,"Le nombre d'éléments du tableau a changé"
    assert temp in tab,"tab[i] a disparu"
    assert tab[i] in tab,"tab[j] a disparu"

    return tab
  
    
def tri_bulles(tab:list)->list:
    """Fonction de tri à bulles
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

    # On récupère la taille du tableau dans une variable
    n = len(tab)

    #preconditions
    assert isinstance(tab,list),"Le parametre n'est pas une liste"
    assert n>0,"La liste est vide"

    # On ne trie le tableau que s'il a plus qu'un seul élément
    if n>=2 :
        # Traverser tous les éléments du tableau
        for i in range(n):
            # INVARIANT :             
            # Les éléments n-i à n sont triés
            #print("i=",i," : ",tab)
            assert isSorted(tab[n-i:n]),"Le tableau n'est pas trié de n-i à n"
            assert len(tab)==n,"Le nombre d'éléments du tableau a changé"            
            for j in range(0, n-i-1):
                # Si l'élément trouvé est plus grand que le suivant on échange les deux
                if tab[j] > tab[j+1] :
                    #tab[j], tab[j+1] = tab[j+1], tab[j]
                    permuteTab_i_j(tab,j,j+1)

    #postconditions
    assert len(tab)==n,"Le nombre d'éléments du tableau a changé"                
    assert isSorted(tab),"Le tableau n'est pas trié"
    # il faudrait vérifier que les éléments sont restés ceux de départ peut être avec une fonction à part ?        

    return tab

if __name__=="__main__" :
    tab_a_trier=[5,4,3,2,1]
    print(tab_a_trier)
    print(tri_bulles(tab_a_trier))