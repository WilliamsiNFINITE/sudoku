# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'solverwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import copy
from numpy import *
from random import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from BruteForceSolver2 import *
from generateur import *

class Ui_SolverWindow(object):

    def solve(self):
        self.updateBoard()
        self.listenonmodif = copy.deepcopy(self.board.tolist())
        self.listemodif=self.board.tolist()
        print("listesol1", self.listenonmodif)
        cpt=0
        for indiceligne,ligne in enumerate(self.listenonmodif):
            for indicecolonne, element in enumerate(ligne):
                print("element",element)
                if element == '':
                    print("reussite")
                    cpt+=1
                    self.listemodif[indiceligne][indicecolonne] = 0

                else:
                    self.listemodif[indiceligne][indicecolonne] = int(element)
        print(cpt)
        print("listsol2",self.listemodif)

        #tableau = array([[0,0,0,0,0,0],[1,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])
        self.generatedBoard = array(solveGen(self.listemodif, self.hauteur, self.largeur)[0])  # DIMENSION
        monarray = self.board
        #print('monarray', monarray, "arraytype", type(monarray))
        maliste = monarray.tolist()
        #print("list",maliste, "typelist", type(maliste))
        deuxiemeBoard = array(solveGen(maliste, self.hauteur, self.largeur)[0])
        #print("2eboard",deuxiemeBoard)


        #print("generated board", self.generatedBoard, "type", type(self.generatedBoard))


        ui.setupUi(SolutionWindowSolver, self.hauteur, self.largeur, "Solution")
        SolutionWindowSolver.show()

    def updateBoard(self):
        """
        This method updates the board to match the values currently displayed on the Sudoku window
        """
        self.board = []
        for i in range(self.dimension):  # row
            for j in range(self.dimension):
                self.board.append(self.boxes[(i, j)].toPlainText())

        self.board = array(self.board)
        self.board = self.board.reshape((self.dimension, self.dimension))
        print("board \n", self.board)

    def setupUi(self, MainWindow, hauteur = 2, largeur=3, case="Empty"):
        print(case)
        self.largeur = largeur
        self.hauteur = hauteur
        self.dimension = self.largeur*self.hauteur

        if case != "Solution":
            self.boxes = {}
            self.board = []
        else :
            self.boardSolver = self.board



        MainWindow.resize(445, 550)

        font = QtGui.QFont()
        font.setPointSize(16)

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)

        brush = QtGui.QBrush(QtGui.QColor(250, 250, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        MainWindow.setPalette(palette)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)

        "This next part defines the Sudoku grid itself"

        yPosition = -30
        for i in range(self.dimension):  # hauteur
            xPosition = -20
            yPosition += 40
            if i % self.hauteur == 0:
                yPosition += 10
            for j in range(self.dimension):
                xPosition += 40

                if j % self.largeur == 0:
                    xPosition += 10

                if ((i // self.hauteur) + (j // self.largeur)) % 2 == 0:
                    brush = QtGui.QBrush(QtGui.QColor(215, 215, 215))
                else:
                    brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
                # brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
                # palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Base, brush)
                self.boxes[(i, j)] = QtWidgets.QPlainTextEdit(self.centralwidget)
                self.boxes[(i, j)].setGeometry(xPosition, yPosition, 41, 41)
                self.boxes[(i, j)].setFont(font)
                self.boxes[(i, j)].setPalette(palette)
                self.boxes[(i, j)].setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
                self.boxes[(i, j)].setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
                self.boxes[(i, j)].setTabChangesFocus(True)
                if case != "Solution":
                    self.boxes[(i, j)].setPlainText("")
                    self.board.append(self.boxes[(i, j)].toPlainText())
                else :
                    self.boxes[(i, j)].setPlainText(str(self.generatedBoard[i][j]))
        # MainWindow.setCentralWidget(self.centralwidget)
        self.board = array(self.board)
        self.board = self.board.reshape((self.dimension, self.dimension))




        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.horizontalLayout.addItem(spacerItem2)
        self.solveButton = QtWidgets.QPushButton(self.centralwidget)
        self.horizontalLayout.addWidget(self.solveButton)

        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayout_2.addLayout(self.verticalLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 445, 26))
        self.menuHELP = QtWidgets.QMenu(self.menubar)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuHELP.menuAction())

        self.solveButton.clicked.connect(self.solve)  # TO CHANGE


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Solver P.P.P.M.H.W."))
        self.solveButton.setText(_translate("MainWindow", "R??soudre"))
        self.menuHELP.setTitle(_translate("MainWindow", "Help"))




if __name__ == "__main__":
    import sys
    appsolver = QtWidgets.QApplication(sys.argv)
    SolutionWindowSolver = QtWidgets.QMainWindow()
    SolutionWindow = QtWidgets.QMainWindow()


    ui = Ui_SolverWindow()
    ui.setupUi(SolutionWindowSolver)
    SolutionWindowSolver.show()
    sys.exit(appsolver.exec_())