import pyxel

class Vehicle(object):
    """
    Classe utilisée pour créer et gérer un véhicule
    """

    def __init__(self, y, isLeft = True):
        """
        Méthonde d'initialisation de la classe Vehicle, permettant de créer et gérer les attributs des véhicules.
        """
        self.x = 120 if isLeft else -10
        self.y = y
        self.isLeft = isLeft
        #Stopping methods
        self.stop = False
        self.stopMultiplier = 0.8

        #car attributes
        self.width = 28
        self.height = 16

    def movement(self, speedMultiplier):
        """
        Méthode pour gérer le déplacement des véhicules.
        """
        if self.stop:
            self.x += 0.7 * speedMultiplier * self.stopMultiplier if self.isLeft else -0.5 * speedMultiplier * self.stopMultiplier
            self.stopMultiplier -= 0.04
        else:
            self.x -= 0.7 * speedMultiplier if self.isLeft else -0.5 * speedMultiplier    
        
    def isOnScreen(self):
        """
        Méthode pour vérifier si le véhicule à dépasser la taille de l'écran
        """
        if self.x < - 50 or self.x > 160 :
            return False
        return True

    def stopVehicle(self):
        """
        Méthode pour stopper les véhicules
        """
        self.stop = True

    def update(self, speedMultiplier):
        """
        Méthode pour mettre à jour le véhicule
        """
        self.movement(speedMultiplier)            

    def draw(self):
        """
        Méthode pour déssiner chaque véhicules sur l'écran.
        """
        if self.isLeft:
            pyxel.blt(self.x, self.y, 0, 2, 88, self.width, self.height, 0)
            pyxel.rect(self.x, self.y, self.width, self.height, 12)
        else:
            pyxel.blt(self.x, self.y, 0, 2, 88, -self.width, self.height, 0)
            pyxel.rect(self.x, self.y, self.width, self.height, 12)