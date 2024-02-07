from direct.showbase.ShowBase import ShowBase

from hero import Hero
from mapmanager import Mapmanager

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()
        x,y = self.land.LoadLand('land.txt')
        base.camLens.setFov(90)
        self.hero = Hero((x//2, y//2,2), self.land)
game = Game()
game.run()