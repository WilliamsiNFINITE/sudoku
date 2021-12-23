import numpy as np 
import time
import random as rd
from tester_grille_final import *
from BruteForceSolver2 import *
import copy


class Generateur(list):

	def __init__(self,hauteur,largeur):
		self.hauteur=hauteur
		self.largeur=largeur
		self.dim=largeur*hauteur
		self=[]

	def generer_vierge(self):
		for j in range(self.dim):
			self.append([])

		for i in range(self.dim):
			for k in range(self.dim):
				self[i].append(0)
		return self

	def une_valeur_hasard(self):
		x = rd.randint(0, self.dim - 1)
		y = rd.randint(0 ,self.dim - 1)
		pos = [x, y]
		val=rd.randint(1,self.dim)
		self[x][y]=val

		return self


	def grille_complete(self):
		board=np.array(self)
		Sol1 = solveGen(board,self.hauteur,self.largeur)[0]
		Sol2 = solveGen_rev(board, self.hauteur, self.largeur)[0]
		tirage=rd.randint(0,1)
		if tirage == 0 :
			for i in range(self.dim):
				for j in range(self.dim):
					self[i][j]=list(Sol1)[i][j]

		else:
			for i in range(self.dim):
				for j in range(self.dim):
					self[i][j]=list(Sol2)[i][j]


		return self


def generation(L,l):
	A=Generateur(L,l)
	A.generer_vierge()
	print(A)
	A.une_valeur_hasard()
	print(A)
	A.grille_complete()
	print(A)
	Sauvegarde=copy.deepcopy(A)
	Lpos=[]
	attempt=0
	while attempt<(L*l)**2:
		while unicite(Sauvegarde,L,l)==True:
			x = rd.randint(0, L * l - 1)
			y = rd.randint(0, L * l - 1)
			pos = [x, y]
			while pos in Lpos:
				break
			Sauvegarde[x][y]=0
			Lpos.append(pos)
		if unicite(Sauvegarde,L,l)==False:
			lastx,lasty=Lpos[-1]
			Sauvegarde[lastx][lasty]=A[lastx][lasty]
			attempt+=1
	print("attempt",attempt)
	return np.array(Sauvegarde)









