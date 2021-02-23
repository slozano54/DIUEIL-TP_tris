#!/usr/bin/python3
#-*- coding: utf8 -*-
"""
    Génère la documentation
"""
pass

# On fait les imports nécessaires selon le contexte
# Pour générer la documentation
import os
# Pour mesurer le temps de traitement du script
from datetime import datetime 


# Script principal
def main():
    # On récupère la date au début du traitement
    start_time = datetime.now()

    # On génère la documentation
    print("=============================================================================")
    print("  Création de la documentation en cours ...  ")    
    print(" ")
    os.system('sh ./generateMyDoc.sh')   

    # On évalue le temps de traitement
    end_time = datetime.now()
    print("=============================================================================")
    print("  Durée de traitement : ",end_time-start_time)        
    print("=============================================================================")
 
if __name__ == "__main__":
    main()