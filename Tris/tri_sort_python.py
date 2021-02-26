#!/usr/bin/python3
#-*- coding: utf8 -*-
"""
    ## Procédure tri sort() de python
"""
pass

#pour copier une variable
import copy 

def fctSort(tab_source:list)->list:
    """
    Mise en forme de la fonction sort pour effectuer le test de mesure de temps.
        
    **Paramètres** tab_source : une liste	
    **Sorties** la liste triée	
    **Exemples**	
    >>> my_tab_to_sort = [5,1,2,4,3]
    [1,2,3,4,5]

    """
    pass

    # On va travailler sur une copie du tableau de manière à pouvoir faire plusieurs appels
    # de la fonction sans modifier le tableau d'origine  
    tab = copy.deepcopy(tab_source)

    # Pour compter les actions atomiques
    spy = 0
    tab.sort()    
    spy +=1 # espion
    
    return [tab,spy]

if __name__=="__main__" :
    tab_a_trier=[5,4,3,2,1]
    print(tab_a_trier)
    print(fctSort(tab_a_trier))
