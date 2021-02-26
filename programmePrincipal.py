#!/usr/bin/python3
#-*- coding: utf8 -*-
"""
    Teste les fonctions de tri
"""
pass

# On fait les imports nécessaires selon le contexte

# Pour mesurer le temps de traitement du script
from datetime import datetime 
# Pour copier les variable
import copy 

# Modules de tri
from Tris.tri_sort_python import fctSort
from Tris.tri_bulles import tri_bulles  
from Tris.tri_bulles_plus import tri_bulles_plus  
from Tris.tri_selection import tri_selection
from Tris.tri_rapide_non_recursif import tri_rapide_non_recursif

# Module mesures de temps
from Tris.mesureTempsTriV3 import *

# Script principal
def main():    
    # On récupère la date au début du traitement
    start_time = datetime.now()    

    print("=============================================================================")    
    print("On génère toutes les listes pour les tests si elles n'existent pas déjà ...")    
    print("")
    #p=12 #exposant de puissance de 2 pour la taille des listes à trier
    p=11 #exposant de puissance de 2 pour la taille des listes à trier
    if (not os.path.exists("./csv_files2test") or len(os.listdir("./csv_files2test")) == 0):
        genereToutesLesListes(3, pow(2,p))
    # Mesures de temps et d'actions atomiques
    print("=============================================================================")    
    print("Mesures de temps et actions atomiques en cours ...  ")
    print("")
    print("=============================================================================")    
    print("On teste la fonction sort de python")    
    tempsTriAleatoire(fctSort, 3, pow(2,p), "resultats_sortListeAleatoire.csv")
    print("=============================================================================")    
    print("On teste la fonction tri_bulles  ")    
    tempsTriAleatoire(tri_bulles, 3, pow(2,p), "resultats_bullesListeAleatoire.csv")        
    print("=============================================================================")    
    print("On teste la fonction tri_bulles_plus  ")    
    tempsTriAleatoire(tri_bulles_plus, 3, pow(2,p), "resultats_bullesPlusListeAleatoire.csv")    
    print("=============================================================================")    
    print("On teste la fonction tri_selection  ")
    tempsTriAleatoire(tri_selection, 3, pow(2,p), "resultats_selectionListeAleatoire.csv")
    print("=============================================================================")    
    print("On teste la fonction tri_rapide_non_recursif  ")
    tempsTriAleatoire(tri_rapide_non_recursif, 3, pow(2,p), "resultats_rapide_non_recursifListeAleatoire.csv")


    # On évalue le temps de traitement
    end_time = datetime.now()
    print("=============================================================================")
    print("  Durée totale de traitement : ",end_time-start_time)        
    print("=============================================================================")
 
if __name__ == "__main__":
    main()
