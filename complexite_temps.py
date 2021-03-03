#!/usr/bin/python3
#-*- coding: utf8 -*-

import time
import random
import copy

def generateurListeCsv(tri, n, nomFichier):
	"""
	generateurListeCsv prend en paramètres :

	- tri : une chaine de caractère désignant si la liste est triée  d'une certaine manière ou non : prend les valeurs "CROISSANT", "DECROISSANT" ou "ALEATOIRE";
	- n : un entier correspondant au nombre d'éléments dans la liste;
	- nomfichier : une chaine de caractères correspondant au nom de fichier en ".csv" ( ex : "toto.csv" )

	generateurListeCsv génère un fichier csv contenant une liste d'entier triée croissante, décroissante ou non triée.
	"""
	pass

	fichier=open(nomFichier,"w")
	if tri.lower()=="croissant" :
		i=0
		while i<n :
			if i!= n-1 :
				fichier.write(str(i)+";")
			else :
				fichier.write(str(i))
			i=i+1
	elif tri.lower()=="decroissant" :
		i=n-1
		while i>=0 :
			if i!=0 :
				fichier.write(str(i)+";")
			else :
				fichier.write(str(i))
			i=i-1
	else :
		i=0
		while i<n :
			if i!= n-1 :
				fichier.write(str(random.randint(0,n))+";")
			else :
				fichier.write(str(i))
			i=i+1
	fichier.close()

def genereToutesLesListes(nombre, n):
	"""
	genereToutesLesListes prend en paramètre :

	- nombre : entier >=1 correspondant au nombre de listes aléatoires à générer;
	- n : entier correspondant au nombre dentiers dans les listes à générer

	genereToutesLesListes génère des fichiers .csv contenant des listes d'entiers.
	"""
	pass

	generateurListeCsv("croissant",n,"croissant"+str(n)+".csv")
	generateurListeCsv("decroissant",n,"decroissant"+str(n)+".csv")
	for i in range(nombre):
		print("i : "+str(i))
		generateurListeCsv("aleatoire",n,str(i)+"aleatoire"+str(n)+".csv")
				
				
def restitueListe(nomFichier):
	"""
	retitueListe prend en paramètre :
	
	- une chaine de caractères correspondant au nom de fichier csv généré avec la procédure generateurListeCsv.
	
	restitueListe renvoie :
	
	- une liste d'entier
	"""
	pass

	fichier=open(nomFichier,"r")
	ligne=fichier.read()
	l=ligne.split(";")
	n=len(l)
	i=0
	while i<n :
		l[i]=int(l[i])
		i=i+1	
	fichier.close()
	return l
	
	
def mesureTempsExecutionTri(fonctionTri, liste):
	"""
	mesureTempsExecutionTri prend en paramètres :

	- fonctionTri : une fonction de tri prenant en paramètre une liste d'entiers;
	- liste : une liste d'entiers.
	
	mesureTempsExecutionTri renvoie :
	- un flottant correspondant au temps écoulé pour l'exécution de la fonction.
	"""
	pass

	t1=time.time()
	fonctionTri(liste)
	dt=time.time()-t1
	return dt
	
	
def mesure_temps(fonctionTri, nMax, nomFichierRapportCsv, nomListeATrierCsv):
	"""
	mesure_temps prend en paramètres :

	- fonctionTri : une fonction de tri prenant en paramètre une liste d'entiers;
	- nMax : un entier >=1, correspondant à la taille de la plus grande liste à tester;
	- nomFichierRapportCsv : une chaine de caractères correpondant au nom du fichier csv contenant les données à renvoyer comme résultat;
	- nomListeATrierCsv : une chaine de caractères correpondant au nom du fichier csv contenant une liste de données (nombre entiers) à trier, le nombre de données à trier de la liste doit être >= nMax.
	
	mesure_temps affiche le temps mis, et le nombre de tours de boucle effectué par fonctionTri pour effectuer son tri pour différentes longueurs des listes à trier, et génère un fichier csv contenant les résultat de ces mesures et comptages. 
	"""
	pass 

	fichier=open(nomFichierRapportCsv,"w")
	fichier.write("n;"+nomFichierRapportCsv+" t(s)\n")
	print("###################  "+nomFichierRapportCsv+"  #####################################")
	
	tableau=[] #liste de listes de temps pour chaque valeur de n
	tabn=[] #liste des valeurs de n
	
	#mesure des temps d'exécution
	listeAleatoire=restitueListe(nomListeATrierCsv) 
	assert len(listeAleatoire)>=nMax, "liste à traiter trop petite ou nMax trop grand"
	tab=[]     
	n=1	
	while n<=nMax :
		listeATrier=copy.deepcopy(listeAleatoire[:n])
		t=mesureTempsExecutionTri(fonctionTri, listeATrier)
		print("temps pour trier "+str(n)+" entiers d'une liste aléatoire : "+str(t)+" s")
		fichier.write(str(n)+";"+str(t)+"\n")
		n=n*2
	
	fichier.close()

def mesure_complexite(fonctionTri, nMax, nomFichierRapportCsv, nomListeATrierCsv):
	"""
	mesure_complexite prend en paramètres :

	- fonctionTri : une fonction de tri prenant en paramètre une liste d'entiers;
	- nMax : un entier >=1, correspondant à la taille de la plus grande liste à tester;
	- nomFichierRapportCsv : une chaine de caractères correpondant au nom du fichier csv contenant les données à renvoyer comme résultat;
	- nomListeATrierCsv : une chaine de caractères correpondant au nom du fichier csv contenant une liste de données (nombre entiers) à trier, le nombre de données à trier de la liste doit être >= nMax.
	
	mesure_complexite nécessite l'insertion de la fonction compteTourBoucle() au sein de chaque boucle (dans le code de la fonction testée) de la fonction à testée.
	
	mesure_complexite affiche le temps mis, et le nombre de tours de boucle effectué par fonctionTri pour effectuer son tri pour différentes longueurs des listes à trier, et génère un fichier csv contenant les résultat de ces mesures et comptages. 
	"""
	pass
	
	fichier=open(nomFichierRapportCsv,"w")
	fichier.write("n;"+nomFichierRapportCsv+" t(s);"+nomFichierRapportCsv+" opérations\n")
	print("###################  "+nomFichierRapportCsv+"  #####################################")
	
	tableau=[] #liste de listes de temps pour chaque valeur de n
	tabn=[] #liste des valeurs de n
	
	#mesure des temps d'exécution
	listeAleatoire=restitueListe(nomListeATrierCsv) 
	tab=[]     
	n=1	
	while n<=nMax :
		listeATrier=copy.deepcopy(listeAleatoire[:n])
		global spy #espion
		spy=0     #espion
		t=mesureTempsExecutionTri(fonctionTri, listeATrier)
		print("nombre de tours de boucle : "+str(spy))   #espion
		print("temps pour trier "+str(n)+" entiers d'une liste aléatoire : "+str(t)+" s")
		fichier.write(str(n)+";"+str(t)+";"+str(spy)+"\n")
		n=n*2
	
	fichier.close()


def compteTourBoucle():
	"""
	procédure qui incrémente lorsqu'elle est appelée la variable globale spy déclarée dans le programme d'appel : permet de compter les tours de boucle
	"""
	pass

	global spy
	try:
		spy=spy+1
	except NameError :
		pass    

def fctSort(liste):
	"""
	mise en forme de la fonction sort pour effectuer le test de mesure de temps
	"""
	pass

	liste.sort()
	return liste

	

if __name__=="__main__" :
	
	
	p=12 #exposant de puissance de 2 pour la taille des listes à trier
	
	#genereToutesLesListes(1, pow(2,p))
	
	mesure_temps(fctSort, pow(2,p), "testTempsSort.csv", "0aleatoire16777216.csv")
	
	mesure_complexite(fctSort, pow(2,p), "testComplexSort.csv", "0aleatoire16777216.csv")

	
	


