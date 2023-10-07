from direct.showbase.ShowBase import ShowBase

from mapmanager import MapManager

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = MapManager()
        self.land.loadMap("map.txt")
        
        base.camLens.setFov(90)

base = Game()

base.run()
