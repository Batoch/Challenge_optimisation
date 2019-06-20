import csv

position = []
operation = []
Baie = []
Hauteur = []
operations = []


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
#print(position)

with open('1_operations.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        operation.append(row)

operation = operation[1:]
#print(operation)

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
            col, haut = trouvercoloneconteneur(op[0])
            while len(Baie[col]) > haut:
                deplacer(col, premierepilenonpleine())
            retrait(col)




def colonneplein(colonne):          #return 0 si non pleine, 1 sinon
    if len(Baie[colonne]) >= 5:
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
    return len(Baie[colonne])


def trouvercoloneconteneur(nom):
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




firstfit()

ecrituresol()

