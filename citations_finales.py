import numpy.random as rand


" Le code prend en argument un booléen et renvoie une citation selon la valeur du booléen. False est pour l'échec et True pour la réussite." \
"Normalement tout est lisible ! "

def citation(Bool):
    alea=rand.randint(0,9)

    if Bool:
        fil1 = open("citations_reu.txt", "r")
        lignes_reussite=fil1.readlines()
        print(lignes_reussite[alea])


    if not Bool:
        fil2 = open("citations_ech.txt", "r")
        lignes_echec = fil2.readlines()
        print(lignes_echec[alea])


citation(False)
citation(True)