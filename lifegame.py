import random
form pyfiglet import Figlet

g = Figlet(font='slant')
print(g.renderText('CultureG'))

class Personnage:
    def __init__(self, nom):
        self.nom = nom
        self.sante = 100
        self.faim = 0
        self.humeur = 100

    def manger(self):
        self.faim = 0
        print(f"{self.nom} a bien mangé.")

    def dormir(self):
        self.humeur += 20
        print(f"{self.nom} a bien dormi.")

    def jouer(self):
        self.humeur += 10
        self.faim += 10
        print(f"{self.nom} s'est bien amusé.")

    def statut(self):
        print(f"Nom: {self.nom}")
        print(f"Santé: {self.sante}")
        print(f"Faim: {self.faim}")
        print(f"Humeur: {self.humeur}")

def main():
    nom = input("Choisissez un nom pour votre personnage : ")
    joueur = Personnage(nom)

    while joueur.sante > 0:
        print("\nQue voulez-vous faire ?")
        print("1. Manger")
        print("2. Dormir")
        print("3. Jouer")
        print("4. Quitter")

        choix = input("Entrez le numéro de votre choix : ")

        if choix == "1":
            joueur.manger()
        elif choix == "2":
            joueur.dormir()
        elif choix == "3":
            joueur.jouer()
        elif choix == "4":
            print("Merci d'avoir joué !")
            break
        else:
            print("Choix invalide. Veuillez entrer un numéro de choix valide.")

        # Le personnage perd un peu de santé à chaque tour
        joueur.sante -= random.randint(1, 5)
        joueur.faim += 5

        joueur.statut()

if __name__ == "__main__":
    main()
