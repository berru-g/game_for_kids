import random
from pyfiglet import Figlet

g = Figlet(font='slant')
print(g.renderText('CultureG'))

class Question:
    def __init__(self, question, reponse):
        self.question = question
        self.reponse = reponse

themes = {
    "Math": [Question("2 + 2 =", "4"), Question("9 * 7 =", "63"), Question("12 / 3 =", "4")],
    "Logique": [Question("Quel est le prochain nombre dans cette séquence : 2, 4, 8, 16, ...", "32"), Question("Si tous les chats sont bleus, et Félix est un chat, quelle couleur est Félix ?", "Bleu")],
    "Culture générale": [Question("Quelle est la capitale de la France ?", "Paris"), Question("Qui a peint la Joconde ?", "Léonard de Vinci")],
    "Science": [Question("Quel gaz compose principalement l'atmosphère terrestre ?", "Azote"), Question("Quelle est la formule chimique de l'eau ?", "H2O")],
    "Bien-être": [Question("Quel est le principal avantage de la méditation ?", "Réduction du stress"), Question("Combien d'heures de sommeil recommande-t-on pour une bonne santé ?", "7-8 heures")]
}

def poser_question(theme):
    question = random.choice(themes[theme])
    print("Thème:", theme)
    print(question.question)
    reponse_joueur = input("Votre réponse : ").strip().lower()
    if reponse_joueur == question.reponse.lower():
        print("Bonne réponse !")
        return 1
    else:
        print("Mauvaise réponse. La réponse correcte était:", question.reponse)
        return 0

def jeu_de_memoire():
    score = 0
    themes_disponibles = list(themes.keys())

    for i in range(5):
        theme = random.choice(themes_disponibles)
        themes_disponibles.remove(theme)
        score += poser_question(theme)

    print("Votre score final est de", score, "sur 5.")

if __name__ == "__main__":
    print("Bienvenue dans le jeu de mémoire ! Vous allez répondre à des questions sur divers thèmes.")
    jeu_de_memoire()
