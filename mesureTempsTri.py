import time

def generateurListeCsv(tri, n, nomFichier):
	'''
	generateurListeCsv prend en paramètres :
		- tri : une chaine de caractère désignant si la liste est triée  d'une certaine manière ou non : prend les valeurs "CROISSANT", "DECROISSANT" ou "ALEATOIRE";
		- n : un entier correspondant au nombre d'éléments dans la liste;
		- nomfichier : une chaine de caractères correspondant au nom de fichier en ".csv" ( ex : "toto.csv" )
	generateurListeCsv génère un fichier csv contenant une liste d'entier triée croissante, décroissante ou non triée.
	'''
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
	'''
	genereToutesLesListes prend en paramètre :
		- nombre : entier >=1 correspondant au nombre de listes aléatoires à générer;
		- n : entier correspondant au nombre dentiers dans les listes à générer
	genereToutesLesListes génère des fichiers .csv contenant des listes d'entiers.
	'''
	generateurListeCsv("croissant",n,"croissant"+str(n)+".csv")
	generateurListeCsv("decroissant",n,"decroissant"+str(n)+".csv")
	for i in range(nombre):
		print("i : "+str(i))
		generateurListeCsv("aleatoire",n,str(i)+"aleatoire"+str(n)+".csv")
				
				
def restitueListe(nomFichier):
	'''
	retitueListe prend en paramètre :
		- une chaine de caractères correspondant au nom de fichier csv généré avec la procédure generateurListeCsv.
	restitueListe renvoie :
		- une liste d'entier
	'''
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
	'''
	mesureTempsExecutionTri prend en paramètres :
		- fonctionTri : une fonction de tri prenant en paramètre une liste d'entiers;
		- liste : une liste d'entiers.
	mesureTempsExecutionTri renvoie :
		- un flottant correspondant au temps écoulé pour l'exécution de la fonction.
	'''
	t1=time.time()
	fonctionTri(liste)
	dt=time.time()-t1
	return dt
	
	
def tempsTriAleatoire(fonctionTri, nombreTris, nMax, nomFichierRapportCsv):
	'''
	tempsTri prend en paramètres :
		- fonctionTri : une fonction de tri prenant en paramètre une liste d'entiers;
		- nombreTri : une entier >=1 correspondant aux nombre de tris à effectuer dans le but de faire une moyenne;
		- nMax : une entier >=1 correspondant à la taille de la plus grande liste à tester
		- nomFichierRapportCsv : une chaine de caractères correpondant au nom du fichier csv contenant les données à renvoyer comme résultat
	tempsTri affiche, et génère un fichier csv donnant le temps mis par fonctionTri pour effectuer sont tri en fonction de la longueur des listes testées
	'''
	
	fichier=open(nomFichierRapportCsv,"w")
	
	tableau=[] #liste de listes de temps pour chaque valeur de n
	tabn=[] #liste des valeurs de n
	
	#mesure des temps d'exécution
	for i in range(nombreTris):
		listeAleatoire=restitueListe(str(i)+"aleatoire10000000.csv")      
		n=1	
		while n<=nMax :
			t=mesureTempsExecutionTri(fonctionTri, listeAleatoire[:n])
			print("temps moyen pour trier "+str(n)+" entiers d'une liste aléatoire : "+str(t)+" ms")
			fichier.write(str(n)+";"+str(t)+"\n")
			if i==0 :
				tabn.append(n)
			n=n*10
	
	
	fichier.close()
	
	
def fctSort(liste):
	'''
	mise en forme de la fonction sort pour effectuer le test de mesure de temps
	'''
	liste.sort()

if __name__=="__main__" :
	tempsTriAleatoire(fctSort, 5, 10000000, "sortSurListeAleatoire.csv")
