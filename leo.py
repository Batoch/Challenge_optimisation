import main


def instance():
    for op in main.operation:
        if op[1] == "R":
            colonne, ligne = main.trouverconteneur(op[0])
            if main.taillecolonne(main.Baie[colonne]) == ligne:
                main.retrait(colonne)
            else:
                while main.taillecolonne(main.Baie[colonne]) > ligne:
                    a = 0
                    for i in range(main.L):
                        if i == colonne:
                            i = i+1
                        for j in range(main.taillecolonne(main.Baie[i])):
                            if main.Baie[ligne, main.taillecolonne(main.Baie[colonne])] < main.Baie[i, j]:
                                a = i
                    if a != 0:
                        main.deplacer(colonne, a)
                    else:
                        tab1 = [0, 0]
                        for u in range(main.L):
                            if u == colonne:
                                u = u + 1
                            for v in range(main.taillecolonne(main.Baie[u])):
                                if main.Baie[u, v] < main.Baie[ligne, main.taillecolonne(main.Baie[colonne])]:
                                    if main.Baie[u, v] < tab1[0]:
                                        tab1[0] = main.Baie[u, v]
                                        tab1[1] = u
                        main.deplacer(colonne, tab1[1])
                main.retrait(colonne)
        else:
            b = 0
            for i in range(main.L):
                for j in range(main.taillecolonne(main.Baie[i])):
                    if op[0] < main.Baie[i, j]:
                        b = i
            if b != 0:
                main.ajout(op[0], b)
            else:
                tab2 = [0, 0]
                for l in range(main.L):
                    for c in range(main.taillecolonne(main.Baie[l])):
                        if main.Baie[l, c] < op[0]:
                            if main.Baie[l, c] < tab2[0]:
                                tab2[0] = main.Baie[l, c]
                                tab2[1] = l
                main.ajout(op[0], tab2[1])
        print(main.Baie)

