import random
replay = True

print("Bienvenue dans le Juste Prix !")

# Fonction pour rejouer la partie


def replay_game():
    answer = True
    while answer:
        choice_replay = input("Voulez-vous rejouer ? o/n ")
        if choice_replay == "o":
            print("C'est reparti !")
            answer = False
            return True
        elif choice_replay == "n":
            print("Au-revoir !")
            answer = False
            return False
        else:
            print("Veuillez entrer 'o' ou 'n'")
            answer = True

# Fonction pour tester si la valeur est bien un nombre entier


def tryValue():
    boucle = True
    while boucle:
        choice = input("Veuillez choisir un nombre : ")
        if choice.isdigit():
            boucle = False
        else:
            print("Veuillez entrer un nombre valide !")
            boucle = True
    return int(choice)

# Fonction pour montrer si c'est plus ou moins que le nombre séléctionné aléatoirement


def less_or_more(answer, life):
    print(answer)
    print("Nombre de vie : ", life)
    return answer

# Fonction qui est la base du jeux Juste Prix


def game():
    start = int(input("Choisissez le début de l'intervalle : "))
    end = int(input("Choisissez la fin de l'intervalle : "))
    number = random.randint(start, end)
    life = int(input("Choisissez un nombre de vie : "))
    choice = tryValue()
    while choice != number and life > 0:
        if choice < number:
            life -= 1
            less_or_more("C'est plus !", life)
            choice = tryValue()
        elif choice > number:
            life -= 1
            less_or_more("C'est moins !", life)
            choice = tryValue()

    if life > 0:
        print("Gagné !")
    else:
        print("Perdu !")


# Boucle pour rejouer à l'infi si l'on choisi oui

while replay:
    game()
    replay = replay_game()
