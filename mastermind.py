import random
import time
from pyfiglet import Figlet
from colorama import Fore


f = Figlet(font='larry3D')
print(f.renderText('Master'))
g = Figlet(font='slant')
print(g.renderText('*  mind'))
    
print(Fore.LIGHTBLUE_EX + "Trouve le code")
print(Fore.LIGHTGREEN_EX + "     ****    ")
print(Fore.LIGHTYELLOW_EX + "Gagne le droit de rejouer")

# Générez un code secret aléatoire à 4 chiffres
def generate_secret_code():
    digits = [str(i) for i in range(10)]
    random.shuffle(digits)
    return ''.join(digits[:4])

# Vérifiez si la proposition du joueur est correcte
def check_guess(secret, guess):
    bulls = cows = 0
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows

# Fonction principale du jeu
def main():
    secret_code = generate_secret_code()
    attempts = 0

    while True:
        guess = input(Fore.LIGHTWHITE_EX + "Proposez un code à 4 chiffres : ")
        if len(guess) != 4 or not guess.isdigit():
            print("Veuillez entrer un code à 4 chiffres valide.")
            continue

        bulls, cows = check_guess(secret_code, guess)
        attempts += 1

        if bulls == 4:
            print(Fore.LIGHTRED_EX + f"Bravo ! Vous avez trouvé le code secret en {attempts} tentatives.")
            print(Fore.LIGHTMAGENTA_EX + f"Bravo ! Vous avez trouvé le code secret")
            print(Fore.LIGHTCYAN_EX + f"Bravo !")
            time.sleep(5)
            break
        else:
            print(Fore.LIGHTGREEN_EX + f"Trouvé : {bulls}")
            print(Fore.LIGHTCYAN_EX + f"Mauvaise position : {cows}")

if __name__ == "__main__":
    main()
