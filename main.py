import csv
import numpy as np
from random import *


position = []
operation = []
Hauteur = []
operations = []
operationsopti = []
CT = [0]
numero = 0
nboperation = 0
nboperationmin = 500



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
        position[i][1] = int(position[i][1][1:len(position[i][1])-1])
        position[i][2] = int(position[i][2][1:len(position[i][2])])


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
                    temp = premierepilenonpleine(col+1)
                    while temp == col:
                        temp = premierepilenonpleine(col+1)
                    deplacer(col, temp)
                else:
                    temp = premierepilenonpleine(0)
                    while temp == col:
                        temp = premierepilenonpleine(0)
                    deplacer(col, temp)

            retrait(col)
            operations.append([str(col + 1) + " ", " " + str(0)])
        #print(Baie)
        #print("\n")




def colonneplein(colonne):          #return 0 si non pleine, 1 sinon
    global H
    if taillecolonne(colonne) >= H:
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
    global nboperation
    a = taillecolonne(Colonneactuelle)
    ajout(Baie[Colonneactuelle, taillecolonne(Colonneactuelle)-1], Colonnedesire)
    retrait(Colonneactuelle)
    operations.append([str(Colonneactuelle+1) + " ", " " + str(Colonnedesire+1)])
    nboperation += 1
    #print(Baie)


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
    global L
    i = randint(0, L-2)
    while colonneplein(i):
        i += 1
        while i == L-1:
            i = randint(0, L - 2)
    return i














def ecrituresol(numero):
    with open(str(numero) + '_solution.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

        spamwriter.writerow(['FROM '] + [' TO'])
        for i in range(len(operationsopti)):
            spamwriter.writerow(operationsopti[i])


def init():

    for i in range(len(position)):
        if position[i][1] == 0 and position[i][2] == 0:
            a = 0
        else:
            Baie[position[i][1]-1, position[i][2]-1] = position[i][0]


def estlepluspetit(valeur, colonne):                #val a tester, colonne a tester     return 1 si plus petit; 0 sinon
    global H
    global Baie
    a = 1
    for i in range(taillecolonne(colonne)):
        if int(valeur) > Baie[colonne, i]:
            a = 0
    if taillecolonne(colonne) == 0:
        a = 1
    return a


def instance():
    for op in operation:
        if op[1] == "R":
            colonne, ligne = trouverconteneur(op[0][2:])
            if taillecolonne(colonne) == ligne+1:
                retrait(colonne)
                operations.append([str(colonne + 1) + " ", " " + str(0)])
            else:
                while taillecolonne(colonne) > ligne+1:
                    a = 0
                    for i in range(L-1):
                        if i == colonne:
                            i = i+1
                            if i == L:
                                i = 0
                        for j in range(taillecolonne(i)-1):
                            if Baie[ligne, taillecolonne(colonne)-1] > Baie[i, j]:
                                a = a + 1
                                col = i
                    if a == taillecolonne(colonne):
                        deplacer(colonne, col)
                    else:
                        tab1 = [0, 0]
                        for u in range(L-1):
                            tab1[1] = u
                            if u == colonne:
                                u = u + 1
                                #if u == L:
                                #    u = 0
                            for v in range(taillecolonne(u)-1):
                                if Baie[u, v] < Baie[colonne, taillecolonne(colonne)-1]:
                                    t = 2
                                    if Baie[u, v] > tab1[0]:
                                        tab1[0] = Baie[u, v]
                                        tab1[1] = u
                        if colonne == tab1[1]:
                            tab1[1] = colonne + 1
                            if colonneplein(colonne + 1):
                                tab1[1] = colonne -1
                            if colonne == 4:
                                tab1[1] = 1
                        deplacer(colonne, tab1[1])
                retrait(colonne)
                operations.append([str(colonne + 1) + " ", " " + str(0)])
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
        #print(str(Baie) + "\n")



def instance2():
    for op in operation:
        if op[1] == "A":
            a = 0
            for i in range(L-1):
                if estlepluspetit(op[0][2:], i):
                    a = 1
            if a != 0:
                i = 0
                while colonneplein(i):
                    i += 1
            ajout(op[0][2:], i)
            operations.append([str(0) + " ", " " + str(i + 1)])
        else:
            col, haut = trouverconteneur(op[0][2:])
            while taillecolonne(col)-1 > haut:
                a = 0
                for i in range(L - 1):
                    if estlepluspetit(taillecolonne(col)-1, i):
                        a = 1
                if a == 1 and i != col:
                    deplacer(col, i)
                elif premierepilenonpleine(0) == col:
                    deplacer(col, premierepilenonpleine(col+1))
                else:
                    deplacer(col, premierepilenonpleine(0))
            retrait(col)
            operations.append([str(col + 1) + " ", " " + str(0)])
        ##print(Baie)
        ##print("\n")


def jouer():
    global operationsopti
    global nboperation
    global operations
    global nboperationmin
    nboperation = 0
    operations = []
    init()
    firstfit()

    if nboperation < nboperationmin:
        nboperationmin = nboperation
        operationsopti = operations
        ecrituresol(k)
        print(nboperation)




k = 15
traitementfichier(k)
print("calcul pour le " + str(k))
for i in range(2000):

    jouer()


