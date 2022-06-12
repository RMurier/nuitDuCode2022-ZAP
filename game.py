"""
Le jeu avoidThem est un jeu à obstacle.

Vous incarnerez un petit oiseau, allant rejoindre sa grand-mère, qui attend de l'autre coté de la route.

    - Le personnage doit se déplacer sur la route en utilisant les flèches du clavier, ou les touches ZQSD.
    - Le personnage doit éviter les obstacles.
    - A chaque réussite, la vitesse d'apparition des voitures, ainsi que leurs vitesses seront augmentées.

Vous devez traverser le plus de fois la route en un minimum de temps, tout en essayant de garder des vies.
"""

import pyxel
import random
import datetime

from menu import Menu
from player import Player
from vehicle import Vehicle

class Game(object):
    """
    Classe pour gérer le joueur, les véhicules et leurs attributs.
    """
    def __init__(self):
        self.x = self.y = 128
        
        pyxel.init(self.x, self.y, "Avoid Them", fps=60)
        pyxel.load("assets/avoidThem.pyxres")
        self.menu = Menu()
        self.player = Player()
        self.startTime = None
        self.lstvehicules = []
        self.speedMultiplier = 1
        self.frame = 300
        self.lastVehSpawn = [0, 0, 0, 0]
        self.lvl = 400
        self.levelLabel = 1

        #States
        self.wining = False 
        self.loosing = False

        pyxel.run(self.update, self.draw)

    def win(self):
        self.wining = True
        
    def loose(self):
        self.loosing = True

    def update(self):
        """
        Méthode permettant de gérer les évenements du jeu.
        """
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
        
        if self.menu.isMenu:
            self.menu.update()

        for veh in self.lstvehicules:
            if veh.isOnScreen():
                veh.update(self.speedMultiplier)
            else:
                self.lstvehicules.remove(veh)

        self.player.update(self.lstvehicules)
        rand = random.randint(0, 3)
        if random.randint(0, self.lvl) < 10 and pyxel.frame_count - self.lastVehSpawn[rand] > 60:
            self.lastVehSpawn[rand] = pyxel.frame_count
            if rand == 0:
                newY = 9
                arg = True
            elif rand == 1:
                newY = 31
                arg = False
            elif rand == 2:
                newY = 73
                arg = True
            else:
                newY = 95
                arg = False
            self.lstvehicules.append(Vehicle(newY, arg))
            
        if self.player.y < 9:
            self.player.resetCoords(True)
            self.lvl -= 15
            self.levelLabel += 1

        if self.lvl < 130:
            self.win() 

        if self.player.GetSetLives() == 0:
            self.loose()


    def draw(self):
        """
        Méthode permettant de dessiner le jeu.
        """
        pyxel.cls(0)
        if self.menu.isMenu:
            self.menu.draw()
        else:
            if self.loosing: 
                pyxel.text(50, 64, "GAME OVER", 8)
            elif self.wining:
                pyxel.text("You Win", 50, 50, 11)
            else:
                pyxel.blt(0, 0, 1, 0, 0, 128, 64)
                pyxel.blt(0, 64, 1, 0, 0, 128, 64)
                self.player.draw()
                for veh in self.lstvehicules:
                    veh.draw()
                pyxel.blt(110, 3, 0, 32, 88, 7, 8, 0)
                if self.player.GetSetLives() == 1:
                    pyxel.text(120, 5, str(self.player.GetSetLives()), 8)
                else:
                    pyxel.text(120, 5, str(self.player.GetSetLives()), 7 )
                pyxel.text(5, 2, f"Duree: {round(datetime.datetime.timestamp(datetime.datetime.utcnow()) - self.menu.startPlayFrame, 2)}", 7)
                pyxel.text(5, 120, f"Niveau: {self.levelLabel}", 7)

if __name__ == '__main__':
    game = Game()