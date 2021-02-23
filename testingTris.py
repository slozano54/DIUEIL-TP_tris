#!/usr/bin/python3
#-*- coding: utf8 -*-
"""
    Teste les fonctions de tri
"""
pass

# On fait les imports nécessaires selon le contexte
# Pour mesurer le temps de traitement du script
from datetime import datetime 
# Pour copier
import copy 
# Modules perso
from moduleTris.tri_sort_python import fctSort
from moduleTris.tri_bulles import tri_bulles  
from moduleTris.tri_bulles_plus import tri_bulles_plus  
from moduleTris.tri_selection import tri_selection
from moduleTris.tri_rapide_non_recursif import tri_rapide_non_recursif
# mesures de Temps de Fabien
from moduleTris.mesureTempsTriV3 import *


# Script principal
def main():
    # On récupère la date au début du traitement
    start_time = datetime.now()

    # Tableau à trier
    print("=============================================================================")    
    tab_a_trier=[5,4,3,2,1]
    tab_a_trier_sp=copy.deepcopy(tab_a_trier) # pour la fonction sort() de python
    tab_a_trier_tb=copy.deepcopy(tab_a_trier) # pour la fonction tri_bulles
    tab_a_trier_tbp=copy.deepcopy(tab_a_trier) # pour la fonction tri_bulles_plus
    tab_a_trier_ts=copy.deepcopy(tab_a_trier) # pour la fonction tri_selection
    tab_a_trier_trnr=copy.deepcopy(tab_a_trier) # pour la fonction tri_rapide_non_recursif
    print("tableau à trier : ",tab_a_trier)
    print(" ")

    # On teste tri_bulles()
    print("=============================================================================")
    print("Test de tri_bulles() en cours ...  ")           
    print(tri_bulles(tab_a_trier_tb))    
    print(" ")

    # On teste tri_bulles_plus()
    print("=============================================================================")    
    print("Test de tri_bulles_plus() en cours ...  ")           
    print(tri_bulles_plus(tab_a_trier_tbp))
    print(" ")

    # On teste tri_selection()
    print("=============================================================================")    
    print("Test de tri_selection() en cours ...  ")           
    print(tri_selection(tab_a_trier_ts))
    print(" ")
    
    # On teste tri_rapide_non_recursif()
    print("=============================================================================")    
    print("Test de tri_rapide_non_recursif()) en cours ...  ")           
    print(tri_rapide_non_recursif(tab_a_trier_trnr))
    print(" ")

    # # Tests avec les fonctions de Fabien
    # print("=============================================================================")    
    # print("  Tests avec mesureTempsTri de Fabien en cours ...  ")
    # print("")
    # print("  On génère toutes les listes pour les tests ...  ")
    # #genereToutesLesListes(3, 10000000)
    # print("")
    # print("  On teste la fonction ...  ")
    # #tempsTriAleatoire(fctSort, 3, 10000000, "sortSurListeAleatoire.csv")           

    # Tests avec les fonctions de Fabien
    print("=============================================================================")    
    print("Tests avec mesureTempsTriV3 de Fabien en cours ...  ")
    print("")
    p=12 #exposant de puissance de 2 pour la taille des listes à trier
    print("=============================================================================")    
    print("On génère toutes les listes pour les tests si elles n'existent pas déjà ...")    
    print("") 
    if (not os.path.exists("./csv_files2test")):
        genereToutesLesListes(3, pow(2,p))
    elif (len(os.listdir("./csv_files2test")) == 0):
        genereToutesLesListes(3, pow(2,p))            
    print("")
    print("=============================================================================")    
    print("On teste la fonction sort  ")    
    tempsTriAleatoire(fctSort, 3, pow(2,p), "resultats_sortListeAleatoire.csv")
    print("=============================================================================")    
    print("On teste la fonction tri_bulle_plus  ")
    #tempsTriAleatoire(tri_bulles_plus.tri_bulles_plus, 3, pow(2,p), "resultats_bullesPlusListeAleatoire.csv")
    print("=============================================================================")    
    print("On teste la fonction tri_selection  ")
    #tempsTriAleatoire(triSelection, 3, pow(2,p), "resultats_selectionListeAleatoire.csv")

    # On évalue le temps de traitement
    end_time = datetime.now()
    print("=============================================================================")
    print("  Durée totale de traitement : ",end_time-start_time)        
    print("=============================================================================")
 
if __name__ == "__main__":
    main()