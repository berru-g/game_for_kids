import click
from colorama import Fore, Style, init
from pyfiglet import Figlet
import winsound
import time

init(autoreset=True)
f = Figlet(font='slant')
e = Figlet(font='larry3D')

# Initialisation du score
score = 0

# Fonction pour afficher un indice avec un délai
def afficher_indice(indice, delai=3):
    print(indice)
    time.sleep(delai)
    # click.clear()

# Exercice 1 : Détection d'intrusion
def exercice_detection_intrusion():
    global score  # Utiliser la variable score globale
    click.secho("Jeu 1 : Devinez la Menace", fg="yellow")
    print("Vous devez deviner les types de menaces en utilisant les descriptions et les indices fournis.\n")

    # Description de la menace
    description_menace = "La menace est un logiciel malveillant ou virus très répandu, connu pour voler des informations sensibles."

    # Indice 
    indice1 = "C'est souvent distribué sous forme de pièce jointe dans des e-mails de phishing."
    indice2 = "Il peut se propager rapidement à travers un réseau et causer des dégâts importants."

    print("Description de la menace :")
    print(description_menace)

    # Question
    click.secho("Question : Quel type de menace est-ce ?", fg="cyan")
    reponse_attendue = "virus"

    while True:
        reponse_joueur = input("Votre réponse : ")

        if reponse_joueur.lower() == reponse_attendue:
            winsound.Beep(200, 200)
            winsound.Beep(1000, 200)
            winsound.Beep(200, 200)
            click.secho("Bravo ! Vous avez identifié la menace.", fg="green", bold=True)
            score += 2  # Ajouter 2 points au score
            break
        else:
            click.secho("Réponse incorrecte. Essayez à nouveau.", fg="red")
            afficher_indice(indice1)
            afficher_indice(indice2)
            score -= 1  # Soustraire 1 point du score en cas de mauvaise réponse

    while True:
        ligne_commande = input("Entrez une ligne de commande ou tapez 'help' / 'list' : ")

        if ligne_commande == "scan -net":
            for i in range(20):
                print(Fore.MAGENTA + Style.BRIGHT + "▮" * i, end="\r")
                time.sleep(0.1)
            print(Style.RESET_ALL)
            click.secho("succès.", fg="green", bold=True)
            score += 20  # egg
        elif ligne_commande == "check -system":
            for i in range(20):
                print(Fore.GREEN + Style.BRIGHT + "▮" * i, end="\r")
                time.sleep(0.1)
            print(Style.RESET_ALL)
            click.secho("succès.", fg="green", bold=True)
            score += 3  # Ajouter 3 points au score
        elif ligne_commande == "remove -malware":
            for i in range(20):
                print(Fore.GREEN + Style.BRIGHT + "▮" * i, end="\r")
                time.sleep(0.1)
            print(Style.RESET_ALL)
            click.secho("remove done.", fg="green", bold=True)
            score += 3  # Ajouter 3 points au score
        elif ligne_commande == "help":
            click.secho("Voici quelques commandes utiles :", fg="cyan")
            print("scan -network ou scan -net: pour vérifier si l'intrus est sur le réseau.")
            print("check -system : pour vérifier si l'intrus est sur le système.")
            print("remove -malware : pour prendre des mesures contre la menace.")
        elif ligne_commande == "list":
            print(Fore.CYAN + Style.BRIGHT + f"{f.renderText('Menu')}")
            click.secho("1. Détection d'intrusion", fg="green")
            click.secho("2. Gestion du Pare-feu", fg="green")
            click.secho("3. Collecte des Données", fg="green")
            click.secho("4. Collectez des journaux pour surveiller le réseau", fg="green")
            return  # Revenir au menu principal
        else:
            click.secho("Commande non reconnue. Tapez 'list' ou 'help'.", fg="red")

        click.secho("Passons à l'étape suivante...", fg="cyan")

        if score >= 30:
            click.secho("Votre score est de 30 POINTS BRAVO", fg="green")
            for i in range (10):
                print(Fore.GREEN + Style.BRIGHT + "▮" * i, end="\r")
                time.sleep(0.1)
                winsound.Beep(1000, 200)
            print(Fore.RED + Style.BRIGHT + f"{f.renderText('Good work')}")
            print(Style.RESET_ALL)


# Exercice 2 : Gestion du Pare-feu
def exercice_gestion_pare_feu():
    global score  # Utiliser la variable score globale
    click.secho("Jeu 2 : Configurez le Pare-feu", fg="yellow")
    print("Dans cet exercice, vous allez apprendre à configurer un pare-feu pour protéger le réseau.\n")

    # Description de l'exercice
    description_exercice = "Votre tâche est de configurer un pare-feu pour bloquer les connexions non autorisées vers un serveur web."

    # Indice 1
    indice1 = "Utilisez la commande 'configure -firewall' pour accéder à la configuration du pare-feu."

    # Indice 2
    indice2 = "Ajoutez une règle '-port00' pour autoriser uniquement les connexions sur le port 80."

    print("Description de l'exercice :")
    print(description_exercice)

    # Question
    click.secho("Question : Comment configureriez-vous le pare-feu pour autoriser uniquement les connexions sur le port 80 ?", fg="cyan")
    reponse_attendue = "configure -firewall -port80"

    while True:
        reponse_joueur = input("Votre réponse : ")

        if reponse_joueur.lower() == reponse_attendue:
            for i in range(20):
                print(Fore.GREEN + Style.BRIGHT + "▮" * i, end="\r")
                time.sleep(0.1)
            print(Style.RESET_ALL)
            winsound.Beep(200, 200)
            winsound.Beep(1000, 200)
            winsound.Beep(200, 200)
            click.secho("Bravo ! Vous avez configuré le pare-feu avec succès.", fg="green", bold=True)
            score += 2  # Ajouter 2 points au score
            break
        else:
            click.secho("Réponse incorrecte. Essayez à nouveau.", fg="red")
            afficher_indice(indice1)
            afficher_indice(indice2)
            score -= 1  # Soustraire 1 point du score en cas de mauvaise réponse

    while True:
        ligne_commande = input("Entrez une ligne de commande ou tapez 'help' : ")

        if ligne_commande == "configure -firewall":
            for i in range(20):
                print(Fore.GREEN + Style.BRIGHT + "▮" * i, end="\r")
                time.sleep(0.1)
            print(Style.RESET_ALL)
            click.secho("Succès ! Vous avez accédé à la configuration du pare-feu.", fg="green", bold=True)
            score += 3  # Ajouter 3 points au score
        elif ligne_commande == "add -rule -port80":
            for i in range(20):
                print(Fore.GREEN + Style.BRIGHT + "▮" * i, end="\r")
                time.sleep(0.1)
            print(Style.RESET_ALL)
            click.secho("Succès ! Vous avez ajouté une règle pour autoriser le port 80.", fg="green", bold=True)
            score += 3  # Ajouter 3 points au score
        elif ligne_commande == "help":
            click.secho("Voici quelques commandes utiles :", fg="cyan")
            print("configure -firewall : pour accéder à la configuration du pare-feu.")
            print("add -rule -port80 : pour ajouter une règle pour autoriser le port 80.")
        elif ligne_commande == "list":
            print(Fore.CYAN + Style.BRIGHT + f"{f.renderText('Menu')}")
            click.secho("1. Détection d'intrusion", fg="green")
            click.secho("2. Gestion du Pare-feu", fg="green")
            click.secho("3. Collecte des Données", fg="green")
            click.secho("4. Collectez des journaux pour surveiller le réseau", fg="green")
            return  # Revenir au menu principal
        else:
            click.secho("Commande non reconnue. Tapez 'help'.", fg="red")

        click.secho("Passons à l'étape suivante...", fg="cyan")
        if score >= 30:
            click.secho("Votre score est de 30 POINTS BRAVO", fg="green")
            for i in range (10):
                print(Fore.GREEN + Style.BRIGHT + "▮" * i, end="\r")
                time.sleep(0.1)
                winsound.Beep(1000, 200)
            print(Fore.RED + Style.BRIGHT + f"{f.renderText('Good work')}")
            print(Style.RESET_ALL)
    

# Exercice 3 : Collecte de données
def exercice_collecte_data():
    global score  # Utiliser la variable score globale
    click.secho("Exercice 3 : Collecte de données", fg="cyan", bold=True)
    print("Dans cet exercice, vous allez apprendre à collecter des informations sur le réseau.\n")

    # Description de l'exercice
    description_exercice = "Votre tâche consiste à collecter des informations sur les dispositifs connectés au réseau."

    # Indice 1
    indice1 = "Utilisez la commande 'scan -network' pour lister les dispositifs connectés."

    # Indice 2
    indice2 = "Analysez les résultats pour identifier les dispositifs inconnus ou non autorisés. *egg = scan -net =30pts"

    print("Description de l'exercice :")
    print(description_exercice)

    # Question
    click.secho("Question : Comment collecteriez-vous des informations sur les dispositifs connectés au réseau ?", fg="cyan")
    reponse_attendue = "scan -network"

    while True:
        reponse_joueur = input("Votre réponse : ")

        if reponse_joueur.lower() == reponse_attendue:
            winsound.Beep(200, 200)
            winsound.Beep(1000, 200)
            winsound.Beep(200, 200)
            click.secho("Bravo ! Vous avez collecté des informations sur le réseau.", fg="green", bold=True)
            score += 2  # Ajouter 2 points au score
            break
        else:
            click.secho("Réponse incorrecte. Essayez à nouveau.", fg="red")
            afficher_indice(indice1)
            afficher_indice(indice2)
            score -= 1  # Soustraire 1 point du score en cas de mauvaise réponse

    while True:
        ligne_commande = input("Entrez une ligne de commande ou tapez 'help' : ")

        if ligne_commande == "scan -network":
            for i in range(20):
                print(Fore.GREEN + Style.BRIGHT + "▮" * i, end="\r")
                time.sleep(0.1)
            print(Style.RESET_ALL)
            click.secho("Succès ! Vous avez listé les dispositifs connectés au réseau.", fg="green", bold=True)
            score += 3  # Ajouter 3 points au score
        elif ligne_commande == "analyze -results":
            for i in range(20):
                print(Fore.GREEN + Style.BRIGHT + "▮" * i, end="\r")
                time.sleep(0.1)
            print(Style.RESET_ALL)
            click.secho("Succès ! Vous avez analysé les résultats et identifié des dispositifs non autorisés.", fg="green", bold=True)
            score += 3  # Ajouter 3 points au score
        elif ligne_commande == "help":
            click.secho("Voici quelques commandes utiles :", fg="cyan")
            print("scan -network : pour lister les dispositifs connectés au réseau.")
            print("analyze -results : pour analyser les résultats et identifier des dispositifs non autorisés.")
        elif ligne_commande == "list":
            print(Fore.CYAN + Style.BRIGHT + f"{f.renderText('Menu')}")
            click.secho("1. Détection d'intrusion", fg="green")
            click.secho("2. Gestion du Pare-feu", fg="green")
            click.secho("3. Collecte des Données", fg="green")
            click.secho("4. Collectez des journaux pour surveiller le réseau", fg="green")
            return  # Revenir au menu principal
        else:
            click.secho("Commande non reconnue. Tapez 'help'.", fg="red")

        click.secho("Passons à l'étape suivante...", fg="cyan")
        if score >= 30:
            click.secho("Votre score est de 30 POINTS BRAVO", fg="green")
            for i in range (10):
                print(Fore.GREEN + Style.BRIGHT + "▮" * i, end="\r")
                time.sleep(0.1)
                winsound.Beep(1000, 200)
            print(Fore.RED + Style.BRIGHT + f"{f.renderText('Good work')}")
            print(Style.RESET_ALL)
            
@click.command()
def main():
    global score  # Utiliser la variable score globale
    print(Fore.WHITE + Style.BRIGHT + f"{f.renderText('Hack Learn')}" + Fore.BLUE + f"{f.renderText('---------')}")
    click.secho("Bienvenue dans ton exo system et reseau", fg="green", bold=True)
    click.secho("Ta mission est de faire ces 3 exercices. Réponds à la question '= 1 point' , puis tape les lignes de commande recommandé via la cmd help '= 3 points' ", fg="blue", bold=True)
    click.secho("Si une commande ne fonctionne pas, reviens faire l'exo aprés la prochaine étape.", fg="blue", bold=True)

    print("Tapez 'list' pour afficher tes missions.")

    while True:
        command = input("> ")
        if command == "list":
            click.echo("Options disponibles :")
            click.secho("1. Détection d'intrusion", fg="green")
            click.secho("2. Gestion du Pare-feu", fg="green")
            click.secho("3. Collecte des Données", fg="green")
            click.secho("4. Collectez des journaux pour surveiller le réseau", fg="green")
        elif command == "1":
            exercice_detection_intrusion()
        elif command == "2":
            exercice_gestion_pare_feu()
        elif command == "3":
            exercice_collecte_data()
        elif command == "4":
            exercice_gestion_pare_feu()
        elif command == "exit":
            break
        else:
            click.secho("Commande inconnue. Tapez 'list' pour voir les exercices.", fg="red")

if __name__ == "__main__":
    main()
