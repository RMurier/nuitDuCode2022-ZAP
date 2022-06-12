import pyxel
import datetime

class Player(object):
    """
    Classe pour gérer le personnage et ses attributs
    """

    def __init__(self):
        """
        Méthode pour initialiser les attributs du joueur.
        """
        self.x = 60
        self.y = 115
        self.lives = 999
        self.wait = 180
        #Hit logic 
        self.hitByCar = False
        self.hitLeft = False
        self.hitX = 0
        self.timeSave = 0

        #player attributes
        self.width = 8
        self.height = 4

    def playerDead(self):
        """
        Méthode pour la mort du joueur
        """
        self.resetCoords()
        self.timeSave = 0
        self.hitByCar = False
        self.GetSetLives(False) 

    def resetCoords(self, win=False):
        """
        Méthode pour réinitialiser les coordonnées du joueur.
        """
        if win:
            self.wait = pyxel.frame_count + 60
        self.x = 60
        self.y = 115

    def movement(self):
        """
        Méthode pour gérer les déplacements du joueur.
        """
        if pyxel.frame_count > self.wait + 60:
            if not self.hitByCar:
                if (pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_Q)) and self.x > -2:
                    self.x -= 1
                if (pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D)) and self.x < 115:
                    self.x += 1
                if (pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_Z)) and self.y > -1:
                    self.y -= 1
                if (pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_S)) and self.y < 118:
                    self.y += 1
            else: 
                time = float(datetime.datetime.timestamp(datetime.datetime.utcnow()))
                if self.hitLeft:
                    if self.hitX - 45 < self.x:
                        self.x -= 0.75
                    else :
                        if self.timeSave == 0:
                            self.timeSave = time 
                        elif time > self.timeSave + 1.1:
                            self.playerDead()
                else :
                    if self.hitX + 45 > self.x:
                        self.x += 0.75
                    else :
                        if self.timeSave == 0:
                            self.timeSave = time 
                        elif time > self.timeSave + 1.1:
                            self.playerDead()


    def GetSetLives(self, get=True):
        """
        Méthode / getter et setter pour récupérer ou éditer les vies du joueur
        """
        if not get:
            self.lives -= 1
        return self.lives

    def driveBy(self, vehicule):
        """
        Méthode pour gérer le déplacement du joueur lorsqu'il est touché.
        """
        vehicule.stopVehicle()
        self.hitByCar = True 
        self.hitLeft = vehicule.isLeft
        self.hitX = self.x           

    def checkCollision(self, vehicule):
        """
        Méthode pour vérifier la collision entre le joueur et les véhicules.
        """
        if not self.hitByCar:
            for veh in vehicule:
                if veh.isLeft:
                    if (self.x + self.width >= veh.x and self.x <= veh.x + veh.width) and (self.y + self.height >= veh.y and self.y <= veh.y + veh.height):
                        self.driveBy(veh)
                else:
                    if (self.x + self.width >= veh.x and self.x <= veh.x + veh.width) and (self.y + self.height >= veh.y and self.y <= veh.y + veh.height):
                        self.driveBy(veh)
            
    def update(self, vehicules):
        """
        Méthode pour gérer les déplacements du joueur.
        """
        self.movement()
        self.checkCollision(vehicules)
    
    def draw(self):
        """
        Méthode pour déssiner le personnage sur l'écran.
        """
        if self.hitByCar :
            pyxel.circ(self.x + self.width // 2, self.y + self.height // 2, self.r, 8)
            self.r += 0.04
        else :
            self.r = 0.5
        if self.wait > pyxel.frame_count:
            pyxel.text(30, 60, "Veuillez patienter", 7)
        pyxel.blt(self.x, self.y, 0, 4, 5, self.width, self.height, 0)
        
    
    