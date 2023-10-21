import random
from colorama import Fore, Style, init
from pyfiglet import Figlet
import winsound
import time

init(autoreset=True)
f = Figlet(font='slant')
e = Figlet(font='larry3D')

def poser_question():
    operation = random.choice(["+", "-", "*", "/"])
    nombre1 = random.randint(1, 20)
    nombre2 = random.randint(1, 20)

    question = f"Calculez : {nombre1} {operation} {nombre2} = "
    reponse = eval(f"{nombre1} {operation} {nombre2}")
    
    return question, reponse

def animation():
    print(Fore.MAGENTA + Style.BRIGHT + "Félicitations ! Vous avez atteint 10 bonnes réponses. 😁")
    
    for i in range(20):
        print(Fore.GREEN + Style.BRIGHT + "🎉" * i, end="\r")
        time.sleep(0.1)
    print(Style.RESET_ALL)

def jouer_melodie():
    for i in range(2):
        print(Fore.LIGHTBLUE_EX + "******")
        winsound.Beep(200, 200)
        print(Fore.LIGHTCYAN_EX + "************")
        winsound.Beep(1000, 200)
        print(Fore.LIGHTYELLOW_EX + "******************")
        winsound.Beep(1200, 200)
        print(Fore.LIGHTWHITE_EX + "************")
        winsound.Beep(1000, 200)
        print(Fore.LIGHTMAGENTA_EX + "******")
        winsound.Beep(440, 200)
        time.sleep(1)

def main():
    print(Fore.CYAN + Style.BRIGHT + f"{f.renderText('Math Game')}" + Fore.BLUE + f"{f.renderText('---------')}")
    player_name = input("Entre ton nom de joueur : ")
    print(f"Bienvenue dans le jeu de mathématiques, {player_name} ! Réponds aux questions pour gagner des points.")
    print(Fore.CYAN +"option : tape '-score' pour afficher ton score.")
    print(Fore.CYAN + "+ et - = 1 point")
    print(Fore.CYAN + "* et / = 2 points")
    addition_score = 0
    subtraction_score = 0
    multiplication_score = 0
    division_score = 0
    total_score = 0
    
    while True:
        question, reponse = poser_question()
        print(Fore.YELLOW + question)
        try:
            reponse_joueur = input("Votre réponse : ")
            
            if reponse_joueur == "-score":
                print(Fore.CYAN + f"-----------------------")
                print(Fore.GREEN + f"Score de {player_name} :")
                print(f"Additions : {addition_score} point(s)")
                print(f"Soustractions : {subtraction_score} point(s)")
                print(f"Multiplications : {multiplication_score // 2} point(s)")
                print(f"Divisions : {division_score // 2} point(s)")
                print(Fore.CYAN + f"-----------------------")
                print(Fore.GREEN + f"Score total : {total_score} point(s)")
                print(Fore.CYAN + f"-----------------------")
            else:
                reponse_joueur = float(reponse_joueur)
                if reponse_joueur == reponse:
                    print(Fore.GREEN + "Bonne réponse !")
                    if "+" in question:
                        addition_score += 1
                    elif "-" in question:
                        subtraction_score += 1
                    elif "*" in question:
                        multiplication_score += 2
                    elif "/" in question:
                        division_score += 2
                    total_score = addition_score + subtraction_score + (multiplication_score // 2) + (division_score // 2)
                    if total_score % 10 == 0:
                        animation()
                        jouer_melodie()
                else:
                    print(Fore.RED + f"La réponse correcte était {reponse}.")
        except ValueError:
            print(Fore.RED + "Veuillez entrer un nombre valide ou '-score' pour afficher votre score.")

if __name__ == "__main__":
    main()
