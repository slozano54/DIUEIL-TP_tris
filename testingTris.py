#!/usr/bin/python3
#-*- coding: utf8 -*-
"""
    Génère la documentation
"""
pass

# On fait les imports nécessaires selon le contexte
# Pour mesurer le temps de traitement du script
from datetime import datetime 
# Pour copier
import copy 
#Modules perso
from moduleTris.tri_bulles import tri_bulles  
from moduleTris.tri_bulles_plus import tri_bulles_plus  
from moduleTris.tri_selection import tri_selection
from moduleTris.tri_rapide_non_recursif import tri_rapide_non_recursif



# Script principal
def main():
    # On récupère la date au début du traitement
    start_time = datetime.now()

    # Tableau à trier
    print("=============================================================================")    
    tab_a_trier=[5,4,3,2,1]
    tab_a_trier_tb=copy.deepcopy(tab_a_trier)
    tab_a_trier_tbp=copy.deepcopy(tab_a_trier)
    tab_a_trier_ts=copy.deepcopy(tab_a_trier)
    tab_a_trier_trnr=copy.deepcopy(tab_a_trier)
    print("tableau à trier : ",tab_a_trier)
    print(" ")

    # On teste tri_bulles()
    print("=============================================================================")
    print("  Test de tri_bulles() en cours ...  ")           
    print(tri_bulles(tab_a_trier_tb))
    print(" ")

    # On teste tri_bulles_plus()
    print("=============================================================================")    
    print("  Test de tri_bulles_plus() en cours ...  ")           
    print(tri_bulles_plus(tab_a_trier_tbp))
    print(" ")

    # On teste tri_selection()
    print("=============================================================================")    
    print("  Test de tri_selection() en cours ...  ")           
    print(tri_selection(tab_a_trier_ts))
    print(" ")
    
    # On teste tri_rapide_non_recursif()
    print("=============================================================================")    
    print("  Test de tri_rapide_non_recursif()) en cours ...  ")           
    print(tri_rapide_non_recursif(tab_a_trier_trnr))
    print(" ")

    # On évalue le temps de traitement
    end_time = datetime.now()
    print("=============================================================================")
    print("  Durée de traitement : ",end_time-start_time)        
    print("=============================================================================")
 
if __name__ == "__main__":
    main()