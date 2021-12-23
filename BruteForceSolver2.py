import numpy as np
import copy



def solveGen(board,L,l):
    boardnew=copy.deepcopy(board)
    if L==l:
        sudoku = SudokuCar(boardnew,L)
    else:
        sudoku=SudokuRec(boardnew,L,l)
    result,boulean = sudoku.solve()
    return result,boulean

def solveGen_rev(board,L,l):
    boardnew=copy.deepcopy(board)
    if L==l:
        sudoku = SudokuCar(boardnew,L)
    else:
        sudoku=SudokuRec(boardnew,L,l)
    result,boulean = sudoku.solve_reverse()
    return result, boulean


def unicite(board, L,l):
    if solveGen(board,L,l)[1] == True and solveGen_rev(board,L,l)[1]==True:
        u=(solveGen(board,L,l)[0]==solveGen_rev(board,L,l)[0])
        if u:
            return True
    return False


class SudokuRec:
    result = []
    board = []

    def __init__(self, board,L,l):
        self.board = board
        self.taille=len(board)
        self.L=L
        self.l=l

    def box_start(self,row,col):
        if row >= 0 and row < self.L:
            box_start_row0 = 0
        if row>=self.L:
            box_start_row0 = row - row % self.L
        if col >= 0 and col < self.l:
            box_start_col0 = 0
        if col>=self.l:
            box_start_col0 = col - col % self.l

        return box_start_row0,box_start_col0

    def check(self, row, col, x):
        nbL=self.L
        nbl=self.l
        box_start_row, box_start_col = self.box_start(row, col)

        for i in range(self.taille):
            if self.board[row][i] == x:
                return False
            if self.board[i][col] == x:
                return False

        for r in range(box_start_row, box_start_row + nbL):
            for c in range(box_start_col, box_start_col + nbl):
                if self.board[r][c] == x:
                    return False
        return True

    def solve(self):
        if self.solve_helper(0):
            #print(" Great things are done when men and mountains meet")
            return self.board,True
        else:
            #print("Je vous dirai que je n’ai jamais eu d’échecs dans ma vie. Il n’y a pas eu d’échecs. Il y a eu des leçons épouvantables.")
            return self.board,False

    def solve_helper(self, k):

        nombre=self.taille**2 -1
        if (k > nombre):
            return True

        r = int(k / self.taille)
        c = k % self.taille

        if self.board[r][c] != 0:
            return self.solve_helper(k+1)

        for x in range(1, self.taille+1):

            if self.check(r, c, x):

                self.board[r][c] = x

                if self.solve_helper(k+1):

                    return True

                self.board[r][c] = 0

        return False

    def solve_reverse(self):
        # init the solve_helper at cell (0, 0)
        if self.solve_helper_reverse(0):
            #print(" Rev / Great things are done when men and mountains meet")
            return self.board, True
        else:
            #print("Je vous dirai que je n’ai jamais eu d’échecs dans ma vie. Il n’y a pas eu d’échecs. Il y a eu des leçons effroyables.")
            return self.board, False

    def solve_helper_reverse(self, k):

        nombre=self.taille**2 -1
        if (k > nombre):
            return True

        r = int(k / self.taille)
        c = k % self.taille

        if self.board[r][c] != 0:
            return self.solve_helper_reverse(k+1)

        for x in range(self.taille, 0,-1):


            if self.check(r, c, x):

                self.board[r][c] = x

                if self.solve_helper_reverse(k+1):

                    return True

                self.board[r][c] = 0
        return False



class SudokuCar(SudokuRec):

    def __init__(self,board,c):
        super().__init__(board,c,c)

    def check(self, row, col, x):
        nb = int(np.sqrt(self.taille))
        for i in range(self.taille):
            if self.board[row][i] == x:
                return False
            if self.board[i][col] == x:
                return False
        box_start_row = row - row % nb
        box_start_col = col - col % nb
        for r in range(box_start_row, box_start_row + nb):
            for c in range(box_start_col, box_start_col + nb):
                if self.board[r][c] == x:
                    return False
        return True





problem3=[[4,1,3,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,1,0],[0,0,0,0,0,0],[0,0,0,0,5,0]]


problem4=[[1, 0 ,0 ,0 ,6, 0],
 [0 ,0, 0, 0, 2, 0],
 [0,1 ,0, 3 ,0 ,0],
 [0, 6,0 ,0, 0 ,0],
 [5, 0 ,0 ,0, 0, 0],
 [0, 0 ,2 ,0 ,3 ,0]]


a=solveGen(problem4,3,2)

b=solveGen_rev(problem4,3,2)



"""print(a)
print(b)
print(a==b)
"""

