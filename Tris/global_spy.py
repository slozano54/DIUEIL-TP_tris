#!/usr/bin/python3
#-*- coding: utf8 -*-
"""
    ## Méthodes pour compter le nombre d'actions atomiques

"""
pass

def compteTourBoucle():
	"""
	procédure qui incrémente lorsqu'elle est appelée la variable globale spy déclarée dans le programme d'appel : permet de compter les tours de boucle
	"""
	global spy
	try:
		spy=spy+1
	except NameError :
		pass 