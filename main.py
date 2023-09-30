from direct.showbase.ShowBase import ShowBase


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.model = loader.loadModel("models/environment")
        self.cube = loader.loadModel("models/Cube/Cobe.egg")
        self.cube_texture = loader.LoadTexture("models/Cube")


        self.cube.setTexture(self.cube_texture)
        self.cube.setPos((1,0,0))
        self.cube.setScale(100)
        self.cube.setColor((1,1,1,1))

        self.model.setPos(0,40,0)
        self.model.setScale(0.5)


        base.camLens.setFov(100)
        self.model.reparentTo(render)

base = Game()

base.run()

