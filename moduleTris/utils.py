#!/usr/bin/python3
#-*- coding: utf8 -*-
"""
    Outils pour les tris
"""
pass

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
  
    

if __name__=="__main__" :
    tab1=[5,4,3,2,1]
    tab2=[1,2,3,4,5]    
    #print(isSorted(tab1))
    print(isSorted(tab2))
    print(tab2)
    print(permuteTab_i_j(tab2,2,3))    
