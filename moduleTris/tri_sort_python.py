#!/usr/bin/python3
#-*- coding: utf8 -*-
"""
    ## Procédure tri sort() de python
"""
pass

def fctSort(liste:list)->list:
	"""
Mise en forme de la fonction sort pour effectuer le test de mesure de temps.
	
**Paramètres** liste : une liste	
**Sorties** la liste triée	
**Exemples**	
>>> my_tab_to_sort = [5,1,2,4,3]
[1,2,3,4,5]

    """
	pass

	liste.sort()
	return liste

if __name__=="__main__" :
    tab_a_trier=[5,4,3,2,1]
    print(tab_a_trier)
    print(fctSort(tab_a_trier))
