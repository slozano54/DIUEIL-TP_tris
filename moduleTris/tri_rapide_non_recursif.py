#!/usr/bin/python3
#-*- coding: utf8 -*-
"""
    ## Procédure tri rapide non recursif

    * On choisit un pivot
    * on coupe le tableau en deux
    * On cherche le plus petit indice i tel que tableau[i] soit superieur ou égal au pivot
    * On cherche le plus grand indice j tel que tableau[j] soit inférieur ou égal au pivot
    * si i<j on échange tableau[i] et tableau[j]
    * On recommence

    De cette manière le pivot est à sa place définitive
"""
pass

# On fait les imports nécessaires selon le contexte
if __name__ == "__main__":    
    import utils as ui    
else:
    import moduleTris.utils as ui    


def isGreater(x:int,y:int)->bool:
    """ Fonction booléenne de comparaison"""
    isGreater = False
    if (x > y):
        isGreater = True
    else:
        isGreater = False
    return isGreater

def partition(tab:list, start:int, end:int)->int:
    """
Fonction pour partionner le tableau

**Paramètres**<br>

* tab : une liste
* start : un entier pour l'indice du pivot
* end : un entier pour le second indice

**Sorties** start : un entier l'indice de la place du pivot<br>
**Notes** On commence arbitrairement par le premier élément du tableau en guise de pivot.<br>
**Exemples**	
>>> my_tab_to_sort = [5,1,2,4,3]
[1,2,3,4,5]

    """
    pass

    while start < end:
        # au debut de cette boucle, on partitionne avec start
        while start < end:
            if isGreater(tab[start], tab[end]):
                (tab[start], tab[end]) = (tab[end], tab[start])
                break
            end = end - 1
        # au debut de cette boucle, on partitionne avec end
        while start < end:            
            if isGreater(tab[start], tab[end]):                
                (tab[start], tab[end]) = (tab[end], tab[start])
                break
            start = start + 1
    return start
 
def tri_rapide_non_recursif(tab:list, start=None, end=None)->list:
    """
Tri rapide non récursif.

**Paramètres**

* tab: une liste
* start : un entier par défaut à None
* end : un entier par défaut à None

**Sorties** Le tableau trié

    """
    pass

    # initialiser
    if start is None: start = 0
    if end is None: end = len(tab)
    
    # Au départ l'indice de début et de fin utilisés pour partitionner sont différents
    indiceStack = [start,end]
    
    # Tant qu'ils sont différents on change l'indice du pivot
    while len(indiceStack)>=2:
        end = indiceStack.pop()
        start = indiceStack.pop()        
        i_pivot = partition(tab, start, end-1)
        
        if start < i_pivot:
            indiceStack.append(start)
            indiceStack.append(i_pivot)

        if end > (i_pivot+1):
            indiceStack.append(i_pivot+1)
            indiceStack.append(end)
    return tab    


if __name__=="__main__" :    
    tab_a_trier = [5,4,3,2,1]
    print(tab_a_trier)
    print(tri_rapide_non_recursif(tab_a_trier))    
