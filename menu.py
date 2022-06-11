import pyxel
import datetime

class Menu(object):
    def __init__(self):
        self.isMenu = True
        self.startPlayFrame = 0

    def draw(self):
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

    def update(self):
        if(pyxel.btnr(pyxel.KEY_SPACE)):
            self.isMenu = False
            self.startPlayFrame = datetime.datetime.timestamp(datetime.datetime.utcnow())