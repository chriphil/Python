def verif(tab):
    for i in range(0,3): # les colonnes
        if(tab[i][0]==tab[i][1]==tab[i][2]!=" "):
            print('Le joueur ',tab[i][0], "a gagné")
            return 0

    for i in range(0,3): # les lignes
        if(tab[0][i]==tab[1][i]==tab[2][i]!=" "):
            print('Le joueur ',tab[0][i], "a gagné.")
            return 0

    if(tab[0][0]==tab[1][1]==tab[2][2]!=" "): # les diagonales, on en a deux
        print('Le joueur ',tab[1][1], "a gagné.")
        return 0

    if(tab[0][2]==tab[1][1]==tab[2][0]!=" "):
        print('Le joueur ',tab[1][1], "a gagné.")
        return 0

    for i in range(0,3): # Encore des cases vides ?
        for j in range(0,3):
            if(tab[i][j]==" "):
                return 1
    print("Fin du jeu aucun gagnant.")
    return 0

def tableau(tab):
    print("-------------")
    for i in range(0,3):
        print("|",tab[i][0],"|",tab[i][1],"|",tab[i][2],"|")
        print("-------------")
    return 1

tab =[[" "," "," "],[" "," "," "],[" "," "," "]]
tableau(tab)
j='X'
joueur=["O","X"]
val=0
while(verif(tab)):
    val=abs(val-1)
    case=int(input("Joueur "+joueur[val]+ ", entrez un numéro de case entre 1 et 9: "))-1
    if(not(-1<case<9)):
        continue
    x=case%3
    y=int((case-x)/3)
    if(tab[y][x]==' '):
        tab[y][x]=j
        j='O' if j=='X' else 'X'
    tableau(tab)
