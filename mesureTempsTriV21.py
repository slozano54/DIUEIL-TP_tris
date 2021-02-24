import time
import random
import copy
from moduleTris import utils as ui

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
	fichier.write("n;"+nomFichierRapportCsv+";"+nomFichierRapportCsv+"\n")
	print("###################  "+nomFichierRapportCsv+"  #####################################")
	
	tableau=[] #liste de listes de temps pour chaque valeur de n
	tabn=[] #liste des valeurs de n
	
	#mesure des temps d'exécution
	for i in range(nombreTris):
		listeAleatoire=restitueListe(str(i)+"aleatoire"+str(nMax)+".csv") 
		tab=[]     
		n=1	
		while n<=nMax :
			listeATrier=copy.deepcopy(listeAleatoire[:n])
			global spy #espion
			spy=0     #espion
			t=mesureTempsExecutionTri(fonctionTri, listeATrier)
			print("nombre de tours de boucles : "+str(spy))   #espion
			print("temps pour trier "+str(n)+" entiers d'une liste aléatoire : "+str(t)+" s")
			tab.append([spy, t])
			n=n*2
		tableau.append(tab)
		
	#calcul des moyennes de temps d'exécution et enregistrement dans le fichier csv
	xMax=len(tableau)
	yMax=len(tableau[0])
	y=0
	while y<yMax :
		t=0.0
		s=0  # nombre de tours de boucles
		x=0
		while x<xMax :
			t=t+tableau[x][y][1]
			s=s+tableau[x][y][0]
			x=x+1
		t=t/float(xMax)   #calcul du temps moyen d'exécution
		s=s/float(xMax)   #calcul du nombre moyen de tours de boucles
		s=int(s)
		fichier.write(str(pow(2,y))+";"+str(t)+";"+str(s)+"\n")
		y=y+1
	
	fichier.close()

def compteTourBoucle():
	'''
	procédure qui incrémente lorsqu'elle est appelée la variable globale spy déclarée dans le programme d'appel : permet de compter les tours de boucle
	'''
	global spy
	try:
		spy=spy+1
	except NameError :
		pass    

def permute(liste,i,j):
	'''
	permute les éléments i et j d'une liste
	'''
	m=liste[j]
	liste[j]=liste[i]
	liste[i]=m

def mini(liste):
	'''
	renvoie un tuple contenant la valeur la plus petite et son indice correspondant
	'''
	N=len(liste)
	m=liste[0]
	indiceMini=0
	i=1
	while i<N :
		compteTourBoucle()   #espion
		if m>liste[i]:
			m=liste[i]
			indiceMini=i
		i=i+1
	return (m,indiceMini)
	
def fctSort(liste):
	'''
	mise en forme de la fonction sort pour effectuer le test de mesure de temps
	'''
	liste.sort()
	return liste

	
def triSelection(liste):
	'''
	tri par selection
	'''
	N=len(liste)
	i=0
	while i<N :
		compteTourBoucle()    #espion
		m=mini(liste[i:])
		permute(liste,i,m[1]+i)
		i=i+1
	return liste
	
def triPivot(liste):
	if liste == []:
		return []
	else:
		pivot = liste[0]
		t1 = []
		t2 = []
		for x in liste[1:]:
			compteTourBoucle() #espion
			if x<pivot:
				t1.append(x)
			else:
				t2.append(x)
		return triPivot(t1)+[pivot]+triPivot(t2)

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
            assert ui.isSorted(tab[n-i:n]),"Le tableau n'est pas trié de n-i à n"
            assert len(tab)==n,"Le nombre d'éléments du tableau a changé"
            compteTourBoucle()                                           #espion            
            for j in range(0, n-i-1):
                # Si l'élément trouvé est plus grand que le suivant on échange les deux
                compteTourBoucle()                                           #espion
                if tab[j] > tab[j+1] :
                    permute(tab,j,j+1)
        
    #postconditions
    assert len(tab)==n,"Le nombre d'éléments du tableau a changé"                
    assert ui.isSorted(tab),"Le tableau n'est pas trié"
    # il faudrait vérifier que les éléments sont restés ceux de départ peut être avec une fonction à part ?        

    return tab	


if __name__=="__main__" :
	
	
	p=11 #exposant de puissance de 2 pour la taille des listes à trier
	
	genereToutesLesListes(3, pow(2,p))
	
	tempsTriAleatoire(triPivot, 3, pow(2,p), "pivot.csv")
	
	tempsTriAleatoire(fctSort, 3, pow(2,p), "sort.csv")
	
	tempsTriAleatoire(tri_bulles, 3, pow(2,p), "bulles.csv")
	
	tempsTriAleatoire(triSelection, 3, pow(2,p), "selection.csv")
	
	


