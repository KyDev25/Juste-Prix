import random
replay = True

print("Bienvenue dans le Juste Prix !\n")

# Function to play again


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

# Function to try value


def tryValue(start, end):
    boucle = True
    while boucle:
        choice = input("Veuillez choisir un nombre entre " +
                       str(start) + " et " + str(end) + " : ")
        if choice.isdigit():
            boucle = False
        else:
            print("Veuillez entrer un nombre valide !")
            boucle = True
    return int(choice)

# Function to determinate if number choice are less or more


def less_or_more(answer, life):
    print(answer)
    print("Nombre de vie : ", life)
    return answer

# Functio which is the basis of the game


def game():
    start = int(input("Choisissez le début de l'intervalle : "))
    end = int(input("Choisissez la fin de l'intervalle : "))
    number = random.randint(start, end)
    life = int(input("Choisissez un nombre de vie : "))
    choice = tryValue(start, end)
    while choice != number and life > 0:
        if choice < number:
            life -= 1
            less_or_more("C'est plus !", life)
            choice = tryValue(start, end)
        elif choice > number:
            life -= 1
            less_or_more("C'est moins !", life)
            choice = tryValue(start, end)

    if life > 0:
        print("Gagné !")
    else:
        print("Perdu ! Le nombre était : " + str(number))


# Loop that plays again until the user answers yes

while replay:
    game()
    replay = replay_game()
