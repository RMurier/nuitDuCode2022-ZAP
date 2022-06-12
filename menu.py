import pyxel
import datetime

class Menu(object):
    def __init__(self):
        self.isMenu = True
        self.startPlayFrame = 0
        self.menu = 0

    def draw(self):
        if self.menu == 0:
            pyxel.text(15, 5, "Bienvenue sur Avoid Them !", 7)

            #Informations Button
            pyxel.rect(10, 20, 110, 15, 7)
            pyxel.text(38, 25, "Informations (1)", 8)

            #Rules button
            pyxel.rect(10, 40, 110, 15, 7)
            pyxel.text(50, 45, "Regles (2)", 8)

            #Play Button
            pyxel.rect(10, 90, 110, 15, 7)
            pyxel.text(40, 95, "Jouer (espace)", 8)
        
        elif self.menu == 1:
            pyxel.text(40, 5, "Informations", 7)
            pyxel.text(5, 25, "Ce jeu est un projet fait par", 7)
            pyxel.text(5, 35, "la ZAP (Zyco And Pingouin)", 7)
            pyxel.text(5, 45, "au cours de la nuit du code", 7)
            pyxel.text(5, 55, "du 9 juillet 2022.", 7)
            pyxel.text(5, 65, "La nuit du code est un marathon", 7)
            pyxel.text(5, 75, "python qui met en competition", 7)
            pyxel.text(5, 85, "les etablissements scolaires", 7)
            pyxel.text(5, 95, "francais dans 38 pays.", 7)
            pyxel.text(10, 105, "Jeu inspire de Crossy Road", 9)
            pyxel.text(55, 115, "Page suivante | =>", 7)
            pyxel.text(5, 115, "<= | Retour", 7)

        elif self.menu == 1.1:
            pyxel.text(40, 5, "Informations", 7)
            pyxel.text(5, 25, "La version donne pour le", 7)
            pyxel.text(5, 35, "marathon, ainsi que ses mises", 7)
            pyxel.text(5, 45, "a jour sont disponible sur", 7)
            pyxel.text(5, 55, "github: github.com/Zyco61", 7)
            pyxel.text(5, 75, "Avoid Them a ete cree par :", 7)
            pyxel.text(5, 85, " - Zyco", 12)
            pyxel.text(5, 95, " - Pingouin", 12)
            pyxel.text(5, 115, "<= | Retour", 7)

        elif self.menu == 2:
            pyxel.text(55, 5, "Regles", 7)
            pyxel.text(5, 25, "AvoidThem est un jeu d'obstacle.", 7)
            pyxel.text(5, 35, "Vous incarnerez un petit oiseau", 7)
            pyxel.text(5, 45, "allant rejoindre sa grand-mere,", 7)
            pyxel.text(5, 55, "qui attend de l'autre cote de", 7)
            pyxel.text(5, 65, "la route.", 7)
            pyxel.text(5, 85, "- Le personnage doit se mouvoir", 9)
            pyxel.text(5, 95, "sur la route en utilisant les", 9)
            pyxel.text(5, 105, "fleches du clavier, ou ZQSD", 9)
            pyxel.text(55, 115, "Page suivante | =>", 7)
            pyxel.text(5, 115, "<= | Retour", 7)

        elif self.menu == 2.1:
            pyxel.text(55, 5, "Regles", 7)
            pyxel.text(5, 25, "- Le personnage doit eviter les", 9)
            pyxel.text(5, 35, "obstacles.", 9)
            pyxel.text(5, 55, "- A chaque reussite, la vitesse", 9)
            pyxel.text(5, 65, "d'apparition des voitures, et", 9)
            pyxel.text(5, 75, "iront egalement plus vite.", 9)
            pyxel.text(5, 95, "- Vous avez que 3 vies pour", 9)
            pyxel.text(5, 105, "reussir.", 9)
            pyxel.text(5, 115, "<= | Retour", 7)

    def update(self):
        if self.menu == 0:
            if pyxel.btnr(pyxel.KEY_SPACE):
                self.isMenu = False
                self.startPlayFrame = datetime.datetime.timestamp(datetime.datetime.utcnow())

            elif pyxel.btnr(pyxel.KEY_1):
                self.menu = 1

            elif pyxel.btnr(pyxel.KEY_2):
                self.menu = 2

        elif self.menu == 1:
            if pyxel.btnr(pyxel.KEY_RIGHT):
                self.menu = 1.1
            elif pyxel.btnr(pyxel.KEY_LEFT):
                self.menu = 0
        
        elif self.menu == 1.1:
            if pyxel.btnr(pyxel.KEY_LEFT):
                self.menu = 1

        elif self.menu == 2:
            if pyxel.btnr(pyxel.KEY_LEFT):
                self.menu = 0
            elif pyxel.btnr(pyxel.KEY_RIGHT):
                self.menu = 2.1
        elif self.menu == 2.1:
            if pyxel.btnr(pyxel.KEY_LEFT):
                self.menu = 2
