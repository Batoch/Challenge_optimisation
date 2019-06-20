import csv
import numpy as np

position = []
operation = []
Hauteur = []
operations = []
CT = [0]


with open('1_global.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        taille = row


N = int(taille[0])
L = int(taille[1])
H = int(taille[2])

Baie = np.zeros((L, H))


with open('1_position.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        position.append(row)
position = position[1:]

for i in range(len(position)):
    position[i][0] = position[i][0][2:len(position[i][0])-1]
    position[i][1] = int(position[i][1][1:2])
    position[i][2] = int(position[i][2][1:2])


with open('1_operations.csv', newline='') as csvfile:
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
            ajout(op[0], i)
            operations.append([str(0) + " ", " " + str(i + 1)])
        else:
            col, haut = trouverconteneur(op[0][2:])
            a = taillecolonne(col)-1
            while taillecolonne(col)-1 > haut:
                if premierepilenonpleine(0) == col:
                    deplacer(col, premierepilenonpleine(col+1))
                else:
                    deplacer(col, premierepilenonpleine(0))
            retrait(col)
            operations.append([str(col + 1) + " ", " " + str(0)])
        print(Baie)




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


def ecrituresol():
    with open('1_detailSolution.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

        spamwriter.writerow(['FROM '] + [' TO'])
        for i in range(len(operations)):
            spamwriter.writerow(operations[i])


def init():

    for i in range(len(position)):
        Baie[position[i][1]-1, position[i][2]-1] = position[i][0]


init()

firstfit()

ecrituresol()

