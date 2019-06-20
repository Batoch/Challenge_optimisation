import csv
import numpy as np

position = []
operation = []
Hauteur = []
operations = []
CT = [0]
numero = 0

def traitementfichier(numero):
    global N
    global L
    global H
    global Baie
    global position
    global operation

    position = []
    operation = []

    with open(str(numero) + '_global.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            taille = row


    N = int(taille[0])
    L = int(taille[1])
    H = int(taille[2])

    Baie = np.zeros((L, H))


    with open(str(numero) + '_position.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            position.append(row)
    position = position[1:]

    for i in range(len(position)):
        position[i][0] = position[i][0][2:len(position[i][0])-1]
        position[i][1] = int(position[i][1][1:2])
        position[i][2] = int(position[i][2][1:2])


    with open(str(numero) + '_operations.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            operation.append(row)

    operation = operation[1:]
    for i in range(len(operation)):
        operation[i][0] = operation[i][0][:len(operation[i][0])-1]
        operation[i][1] = operation[i][1][1:2]



def firstfit():
    for op in operation:
        if op[1] == "A":
            i = 0
            while colonneplein(i):
                i += 1
            ajout(op[0][2:], i)
            operations.append([str(0) + " ", " " + str(i + 1)])
        else:
            col, haut = trouverconteneur(op[0][2:])
            while taillecolonne(col)-1 > haut:
                if premierepilenonpleine(0) == col:
                    deplacer(col, premierepilenonpleine(col+1))
                else:
                    deplacer(col, premierepilenonpleine(0))
            retrait(col)
            operations.append([str(col + 1) + " ", " " + str(0)])
        print(Baie)
        print("\n")




def colonneplein(colonne):          #return 0 si non pleine, 1 sinon
    if taillecolonne(colonne) >= 5:
        return 1
    return 0


def retrait(colonne):
    global operations
    Baie[colonne, taillecolonne(colonne)-1] = 0


def ajout(cont, i):                 #ajoute le conteneur cont a la colonne i
    global operations
    Baie[i, taillecolonne(i)] = cont


def deplacer(Colonneactuelle, Colonnedesire):
    global operations
    a = taillecolonne(Colonneactuelle)
    ajout(Baie[Colonneactuelle, taillecolonne(Colonneactuelle)-1], Colonnedesire)
    retrait(Colonneactuelle)
    operations.append([str(Colonneactuelle+1) + " ", " " + str(Colonnedesire+1)])
    print(Baie)


def taillecolonne(colonne):
    for i in range(H):
        if Baie[colonne, i] == [0]:
            return i
    return H


def trouverconteneur(nom):
    for i in range(L):
        for j in range(H):
            if Baie[i, j] == int(nom):
                return i, j


def premierepilenonpleine(i):               #premiere pile non pleine a partir de la pile i
    while colonneplein(i):
        i += 1
    return i


def ecrituresol(numero):
    with open(str(numero) + '_solution.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

        spamwriter.writerow(['FROM '] + [' TO'])
        for i in range(len(operations)):
            spamwriter.writerow(operations[i])


def init():

    for i in range(len(position)):
        Baie[position[i][1]-1, position[i][2]-1] = position[i][0]


def instance():
    for op in operation:
        if op[1] == "R":
            colonne, ligne = trouverconteneur(op[0][2:])
            if taillecolonne(colonne) == ligne+1:
                retrait(colonne)
            else:
                while taillecolonne(colonne) > ligne+1:
                    a = 0
                    for i in range(L-1):
                        if i == colonne:
                            i = i+1
                            if i == L:
                                i = i - 1
                        for j in range(taillecolonne(i)-1):
                            if Baie[ligne, taillecolonne(colonne)-1] < Baie[i, j]:
                                a = i
                    if a != 0:
                        deplacer(colonne, a)
                    else:
                        tab1 = [0, 0]
                        for u in range(L-1):
                            if u == colonne:
                                u = u + 1
                                if u == L:
                                    u = u - 1
                            for v in range(taillecolonne(u)-1):
                                if Baie[u, v] < Baie[ligne, taillecolonne(colonne)-1]:
                                    if Baie[u, v] < tab1[0]:
                                        tab1[0] = Baie[u, v]
                                        tab1[1] = u
                        deplacer(colonne, tab1[1])
                retrait(colonne)
        else:
            b = 0
            for i in range(L):
                for j in range(taillecolonne(i)):
                    if op[0] < Baie[i, j]:
                        b = i
            if b != 0:
                ajout(op[0], b)
            else:
                tab2 = [0, 0]
                for l in range(L):
                    for c in range(taillecolonne(l)):
                        if Baie[l, c] < op[0]:
                            if Baie[l, c] <= tab2[0]:
                                tab2[0] = Baie[l, c]
                                tab2[1] = l
                ajout(op[0], tab2[1])
        print(str(Baie) + "\n")





k = 11
traitementfichier(k)
init()
firstfit()
ecrituresol(k)

