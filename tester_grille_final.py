import numpy as np
import math as m


board_test = np.array([[3,4,1,"a"],[1,2,"",4],[4,3,2,1],[2,1,4,3]])

# erreur block : np.array([[1,2,3,4],[2,3,4,1],[3, 4, 1, 2], [4, 1, 2, 3]])

#print(board_test)

def test_row(board,i):
	"""
	Return True if the row i is correctly filled
	"""
	liste_test = []
	for j in board[i]:
		if j not in liste_test or j =="":
			liste_test.append(j)
		else :
			return False
	return True

def test_column(board,i):
	"""
	Return True if the column i is correctly filled
	"""
	board_transpose = np.transpose(board)
	#print(board_transpose)
	return test_row(board_transpose,i)

def test_block(board,i,j):
	"""
	Return True if the block at the position number (i,j) is correctly filled
	"""
	x_taille,y_taille = board.shape
	pas = int(np.sqrt(x_taille))
	i_deb=i*pas
	i_fin=(i+1)*pas
	j_deb=j*pas
	j_fin=(j+1)*pas
	block=board[i_deb:i_fin,j_deb:j_fin]
	dict={}
	for i in range(pas):
		for j in range(pas):
			case=block[i][j]
			if case in dict:
				dict[case]+=1
			elif case != "":
				dict[case]=1
	if 2 in dict.values():
		return False
	else:
		return True

def test_valeur(board):
	"""
	Checks if value is a number between 1 and 9
	"""
	dimension = np.sqrt(np.size(board))
	print(dimension)
	liste_valeur = [i for i in range(1,int(dimension+1))]
	for indiceligne, ligne in enumerate(board):
		for indicecolonne, element in enumerate(ligne):
			if element not in liste_valeur:
				return False
	return True

def test_total(board):
	"""
	Checks if the player wins
	"""
	x_taille, y_taille = board.shape
	liste_valeur = [str(l) for l in range(1, x_taille + 1)]
	print("liste", liste_valeur)
	for row in board:
		for x in row:
			if x == "":
				return "a" #None
			elif x not in liste_valeur:
				print("x",x)
				return "b" #0
	for i in range(x_taille):
		if not test_row(board,i):
			return "c" #False #, i, "row"
	for j in range(y_taille):
		if not test_column(board,j):
			return "d" #False # j, "column"
	n = int(np.sqrt(x_taille))
	for i in range(n):
		for j in range(n):
			if not test_block(board,i,j):
				return "e" # False #, i, j, "block"
	
	return "f"  #True

"""a = test_total(board_test)
print(a)"""
"""a = test_total(board_test)
print(a)
print(board_test)"""