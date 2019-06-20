import csv

position = []
operation = []
Baie = []
Hauteur = []
operations = []
CT = [0, 0, 0]

with open('1_global.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        taille = row

#print(taille)
N = int(taille[0])
L = int(taille[1])
H = int(taille[2])


with open('1_position.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        position.append(row)
position = position[1:]

for i in range(len(position)):
    position[i][0] = position[i][0][:len(position[i][0])-1]
    position[i][1] = int(position[i][1][1:2])
    position[i][2] = int(position[i][2][1:2])


with open('1_operations.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        operation.append(row)

operation = operation[1:]
for i in range(len(operation)):
    operation[i][0] = operation[i][0][:3]
    operation[i][1] = operation[i][1][1:2]




# for i in range(H):       #Hauteur
#     Hauteur.append(0)
#
# for i in range(L):      #Largeur
#     Baie.append(Hauteur)








def firstfit():
    for op in operation:
        if op[1] == "A":
            i = 0
            while colonneplein(i):
                i += 1
            ajout(op[0], i)
        else:
            col, haut = trouverconteneur(op[0])
            while taillecolonne(Baie[col]) > haut:
                deplacer(col, premierepilenonpleine())
            retrait(col)




def colonneplein(colonne):          #return 0 si non pleine, 1 sinon
    if taillecolonne(Baie[colonne]) >= 5:
        return 1
    return 0


def retrait(colonne):
    global operations
    Baie[colonne][taillecolonne(colonne)].remove()
    operations += [colonne, 0]


def ajout(cont, i):                 #ajoute le conteneur cont a la colonne i
    global operations
    Baie[i].append(cont)
    operations += [0, i]


def deplacer(Colonneactuelle, Colonnedesire):
    global operations
    ajout(Baie[Colonneactuelle][taillecolonne(Colonneactuelle)], Colonnedesire)
    Baie[Colonneactuelle][taillecolonne(Colonneactuelle)].remove()
    operations += [Colonneactuelle, Colonnedesire]


def taillecolonne(colonne):
    for i in range(H):
        if i > H:
            return H
        if Baie[colonne][i] == [0, 0, 0]:
            return i


def trouverconteneur(nom):
    for i in range(L):
        for j in range(H):
            print(Baie[i][j])
            if Baie[i][j] == nom:
                return i, j


def premierepilenonpleine():
    i = 0
    while colonneplein(i):
        i += 1
    return i


def ecrituresol():
    with open('1_detailSolutiontest.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

        spamwriter.writerow(['FROM'] + ['TO'])
        for i in range(len(operations)):
            spamwriter.writerow(operations[i])


def init():
    for j in range(H):
        Hauteur.append(CT)
    for i in range(L):
        Baie.append(Hauteur)
    print(Hauteur)
    print(Baie)
    for i in range(len(position)):
        print(position[i][1])
        Baie[position[i][1]-1][position[i][2]-1] = [position[i][0]]


init()

firstfit()

ecrituresol()

