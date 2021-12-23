import unittest
from BruteForceSolver2 import *
from generateur import *

class TestBruteForceSolver2(unittest.TestCase):

    def setUp(self):
        self.Car2 = [[0, 0, 3, 0], [0, 4, 0, 0], [0, 1, 0, 0], [0, 0, 2, 0]]
        self.Car3 = [[0, 2, 0, 0, 5, 0, 7, 0, 0],
                    [0, 0, 0, 7, 0, 9, 0, 0, 0, ],
                    [0, 8, 0, 1, 0, 0, 0, 0, 6],
                    [0, 0, 0, 0, 4, 0, 0, 9, 8],
                    [3, 0, 4, 0, 9, 0, 5, 0, 0],
                    [0, 0, 7, 0, 0, 0, 2, 0, 0],
                    [5, 0, 0, 0, 0, 0, 0, 0, 2],
                    [0, 0, 2, 0, 0, 0, 8, 7, 0],
                    [0, 0, 0, 6, 1, 0, 0, 0, 0]]
        self.Rect32 = [[4, 1, 3, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 5, 0]]
        self.Rect23 = [[1, 0, 0, 0, 6, 0],
                    [0, 0, 0, 0, 2, 0],
                    [0, 1, 0, 3, 0, 0],
                    [0, 6, 0, 0, 0, 0],
                    [5, 0, 0, 0, 0, 0],
                    [0, 0, 2, 0, 3, 0]]

        self.car2=SudokuCar(self.Car2,2)
        self.car3=SudokuCar(self.Car3,3)
        self.rect32=SudokuRec(self.Rect32,3,2)
        self.rect23=SudokuRec(self.Rect23,2,3)


    def testInit(self):
        a = self.car2
        b = self.car3
        c = self.rect32
        d = self.rect23

        self.assertEqual(a.L,2)
        self.assertEqual(a.l, 2)
        self.assertEqual(a.taille, a.L*a.l)

        self.assertEqual(b.L,3)
        self.assertEqual(b.l, 3)
        self.assertEqual(b.taille, b.L * b.l)

        self.assertEqual(c.L,3)
        self.assertEqual(c.l, 2)
        self.assertEqual(c.taille, c.L * c.l)

        self.assertEqual(d.L,2)
        self.assertEqual(d.l, 3)
        self.assertEqual(d.taille, d.L * d.l)


    def testboxstart(self):
        a = self.car2
        b = self.car3
        c = self.rect32
        d = self.rect23

        tuplea=a.box_start(2,2)
        tupleb=b.box_start(6,5)
        tuplec=c.box_start(2,4)
        tupled=d.box_start(2,2)

        self.assertEqual(tuplea,(2,2))
        self.assertEqual(tupleb,(6,3))
        self.assertEqual(tuplec, (0, 4))
        self.assertEqual(tupled, (2, 0))


    def testsolve(self):
        a = self.car2
        b = self.car3
        c = self.rect32
        d = self.rect23

        Sola=a.solve()
        sola=Sola[0]
        solabool=Sola[1]
        Solb=b.solve()
        solb=Solb[0]
        solbbool=Solb[1]
        Solc=c.solve()
        solc=Solc[0]
        solcbool=Solc[1]
        Sold=d.solve()
        sold=Sold[0]
        soldbool=Sold[1]

        self.assertIsInstance(Sola[0],list)
        self.assertIsInstance(sola[0],list)
        self.assertTrue(solabool)

        self.assertIsInstance(Solb[0],list)
        self.assertIsInstance(solb[0],list)
        self.assertTrue(solbbool)


        self.assertIsInstance(Solc[0],list)
        self.assertIsInstance(solc[0],list)
        self.assertTrue(solcbool)

        self.assertIsInstance(Sold[0],list)
        self.assertIsInstance(sold[0],list)
        self.assertTrue(soldbool)


    def testsolve_reverse(self):
        
        a = self.car2
        b = self.car3
        c = self.rect32
        d = self.rect23

        Sola=a.solve_reverse()
        sola=Sola[0]
        solabool=Sola[1]
        Solb=b.solve_reverse()
        solb=Solb[0]
        solbbool=Solb[1]
        Solc=c.solve_reverse()
        solc=Solc[0]
        solcbool=Solc[1]
        Sold=d.solve_reverse()
        sold=Sold[0]
        soldbool=Sold[1]

        self.assertIsInstance(Sola[0],list)
        self.assertIsInstance(sola[0],list)
        self.assertTrue(solabool)

        self.assertIsInstance(Solb[0],list)
        self.assertIsInstance(solb[0],list)
        self.assertTrue(solbbool)


        self.assertIsInstance(Solc[0],list)
        self.assertIsInstance(solc[0],list)
        self.assertTrue(solcbool)

        self.assertIsInstance(Sold[0],list)
        self.assertIsInstance(sold[0],list)
        self.assertTrue(soldbool)


    def testunicite(self):

        self.assertTrue(unicite(self.Car2,2,2))
        self.assertTrue(unicite(self.Car3,3,3))
        self.assertFalse(unicite(self.Rect32,3,2))
        self.assertTrue(unicite(self.Rect23,2,3))

class TestGenerateur(unittest.TestCase):

    def setUp(self):
        self.A=Generateur(2,2)
        self.B=Generateur(3,3)
        self.C=Generateur(3,2)
        self.D=Generateur(2,3)

    def testInit(self):
        self.assertEqual(self.A.largeur,2)
        self.assertEqual(self.A.hauteur,2)
        self.assertEqual(self.A.dim, 4 )

        self.assertEqual(self.B.largeur,3)
        self.assertEqual(self.B.hauteur,3)
        self.assertEqual(self.B.dim, 9)  

        self.assertEqual(self.C.largeur,2)
        self.assertEqual(self.C.hauteur,3)
        self.assertEqual(self.C.dim, 6)

        self.assertEqual(self.D.largeur,3 )
        self.assertEqual(self.D.hauteur,2 )
        self.assertEqual(self.D.dim, 6)


        self.assertIsInstance(self.A,list)
        self.assertIsInstance(self.B,list)
        self.assertIsInstance(self.C,list)
        self.assertIsInstance(self.D,list)

    def testGenerervierge_et_valeurhasard(self):
        self.A.generer_vierge()

        for i in range(self.A.dim):
            for k in range(self.A.dim):
                self.assertEqual(self.A[i][k],0)

        self.B.generer_vierge()

        for i in range(self.B.dim):
            for k in range(self.B.dim):
                self.assertEqual(self.B[i][k],0)

        self.C.generer_vierge()

        for i in range(self.C.dim):
            for k in range(self.C.dim):
                self.assertEqual(self.C[i][k],0)

        self.D.generer_vierge()

        for i in range(self.D.dim):
            for k in range(self.D.dim):
                self.assertEqual(self.D[i][k],0)



        self.A.une_valeur_hasard()
        cpt=0
        for i in range(self.A.dim):
            for k in range(self.A.dim):
                if self.A[i][k]!=0:
                    cpt +=1
        self.assertEqual(cpt,1 )

    def testgeneration(self):

         for k in range(2,4):
             for j in range(2,4):
                 A=generation(k,j)
                 B=A.tolist()
                 self.assertIsInstance(B,list)
                 self.assertIsInstance(B[0],list)
                 self.assertTrue(unicite(B,k,j))

               
if __name__ == '__main__':
    unittest.main()



