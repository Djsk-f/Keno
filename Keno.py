import random
def keno ():
    list = []
    incremente = 0
    essai = 0
    print(
        'Bienvenue au jeu du Keno\n le principe du jeu c\'est de trouver 03 combinaison de nombre parmis ceux tirer au hasard de 1 à 80')

    nbr1 = int(input("entrer votre premier nombre\t"))
    nbr2 = int(input("entrer votre second nombre\t"))
    nbr3 = int(input("entrer votre troizieme nombre\t"))

    while incremente != 20:
        essai = random.randint(1, 80)
        list.append(essai)
        incremente += 1
    print(list, '\n')
    print(nbr1, nbr2, nbr3)
    if nbr1 in list and nbr2 in list and nbr3 in list:
        print('Bravo !!! Vous avez gagné au jeu du Keno')
    else:
        print('Desolé vous avez perdu')
keno()