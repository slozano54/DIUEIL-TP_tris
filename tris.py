#!/usr/bin/python3
#-*- coding: utf8 -*-

import complexite_temps

######## outils  #################################################################################

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
    #assert isTrue==True,"Le tableau n'est pas trié"
    #En fait non sinon je ne peux pas m'en servir

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
    
######## fonctions de tri  ###############################################################################

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
            complexite_temps.compteTourBoucle()                                           #espion            
            for j in range(0, n-i-1):
                # Si l'élément trouvé est plus grand que le suivant on échange les deux
                complexite_temps.compteTourBoucle()                                           #espion
                if tab[j] > tab[j+1] :
                    #tab[j], tab[j+1] = tab[j+1], tab[j]
                    permuteTab_i_j(tab,j,j+1)
        
    #postconditions
    assert len(tab)==n,"Le nombre d'éléments du tableau a changé"                
    assert isSorted(tab),"Le tableau n'est pas trié"
    # il faudrait vérifier que les éléments sont restés ceux de départ peut être avec une fonction à part ?        

    return tab

def isGreater(x:int,y:int)->bool:
    """ Fonction booléenne de comparaison"""
    isGreater = False
    if (x > y):
        isGreater = True
    else:
        isGreater = False
    return isGreater

def partition(tab, start, end):
    while start < end:
        # au debut de cette boucle, on partitionne avec start
        complexite_temps.compteTourBoucle()                                           #espion
        while start < end:
            complexite_temps.compteTourBoucle()                                           #espion
            if isGreater(tab[start], tab[end]):
                (tab[start], tab[end]) = (tab[end], tab[start])
                break
            end = end - 1
        # au debut de cette boucle, on partitionne avec end
        while start < end:            
            complexite_temps.compteTourBoucle()                                           #espion
            if isGreater(tab[start], tab[end]):                
                (tab[start], tab[end]) = (tab[end], tab[start])
                break
            start = start + 1
    return start
 
def tri_rapide_non_recursif(tab, start=None, end=None):
    """
    Tri rapide non récursif.

    **Paramètres**

    * tab_source: une liste
    * start : un entier par défaut à None
    * end : un entier par défaut à None

    **Sorties** Le tableau trié
    """
<<<<<<< HEAD

=======
    
>>>>>>> 7d74c1683c9e5535439f5f5b8cc509cbc1bd5548
    pass
    # initialiser
    if start is None: start = 0
    if end is None: end = len(tab)
    
    # Au départ l'indice de début et de fin utilisés pour partitionner sont différents
    indiceStack = [start,end]
    
    # Tant qu'ils sont différents on change l'indice du pivot
    while len(indiceStack)>=2:
        complexite_temps.compteTourBoucle()                                           #espion
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
            complexite_temps.compteTourBoucle()                                           #espion
            while (j<=n-1):
                # si on trouve un plus petit élément on modifie l'indice i_min
                complexite_temps.compteTourBoucle()                                           #espion
                if tab[j] < tab[i_min]:
                    i_min = j
                # incrémenter le compteur boucle secondaire
                j+=1
            # si on a modifié i_min on échange les éléments
            if (i_min != i):
                permuteTab_i_j(tab,i,i_min)
            # incrémenter le compteur boucle principale
            i+=1
    
    # on retourne le tableau trié
    return tab    

def tri_sort(tab:list)->list:
    """
    mise en forme de la fonction sort pour effectuer le test de mesure de temps
    """
    pass

    tab.sort()
    return tab

if __name__=="__main__":    
    # pour générer les csv
    p=24 #exposant de puissance de 2 pour la taille des listes à trier    
    complexite_temps.genereToutesLesListes(1, pow(2,p))

    #pour les tests
    p=8 #exposant de puissance de 2 pour la taille des listes à trier
    
    complexite_temps.mesure_temps(tri_rapide_non_recursif, pow(2,p), "tempsPivot.csv", "0aleatoire16777216.csv")
    
    complexite_temps.mesure_complexite(tri_rapide_non_recursif, pow(2,p), "complexPivot.csv", "0aleatoire16777216.csv")
    
    # complexite_temps.mesure_temps(tri_bulles, pow(2,p), "tempsBulles.csv", "0aleatoire16777216.csv")
    
    # complexite_temps.mesure_complexite(tri_bulles, pow(2,p), "complexBulles.csv", "0aleatoire16777216.csv")

    # complexite_temps.mesure_temps(tri_selection, pow(2,p), "tempsSelection.csv", "0aleatoire16777216.csv")
    
    # complexite_temps.mesure_complexite(tri_selection, pow(2,p), "complexSelection.csv", "0aleatoire16777216.csv")
    
    # complexite_temps.mesure_temps(tri_sort, pow(2,p), "tempsSort.csv", "0aleatoire16777216.csv")
    
    # complexite_temps.mesure_complexite(tri_sort, pow(2,p), "complexSort.csv", "0aleatoire16777216.csv")









