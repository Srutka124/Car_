class Hero:
    def __init__(self, pos, land):
        self.land = land
        self.hero = loader.loadModel('smiley')
        self.hero.setColor((0.2, 0.2, 0.2, 0))
        self.hero.setScale(0.3)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.accept_events()

    def cameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.setH(120)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0,0,1.5)
        self.cameraOn = True
    
    def cameraUp(self):
        base.camera.reparentTo(render)
        base.mouseInterfaceNode.setPos(self.hero.getPos())
        base.enableMouse()
        self.cameraOn = False

    def changView(self):
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()

    def check_dir(self, angle):
        if angle >= 0 and angle <= 20:
            return (0, -1)
        elif angle <= 65:
            return (1, -1)
        elif angle <= 110:
            return (1, 0)
        elif angle <= 155:
            return (1, 1)
        elif angle <= 200:
            return (0, 1)
        
    def lookAt(self, angle):
        x = round(self.hero.getX())
        y = round(self.hero.getY())
        z = round(self.hero.getZ())

        dx, dy = self.check_dir(angle)
        return x+dy, y+dy, z
    
    def forward(self):
        angle = ((self.hero.getH() + 180) % 360)
        pos = self.lookAt(angle)
        self.hero.setPos(pos)

    def turnLeft(self):
        self.hero.setH((self.hero.getH()+5) % 360)

    def turnRight(self):
        self.hero.setH((self.hero.getH()-5) % 360)

    def accept_events(self):
        base.accept('n', self.turnLeft)
        base.accept('n-repeat', self.turnLeft)
        base.accept('m', self.turnRight)
        base.accept('m-repeat', self.turnRight)
        base.accept('c', self.changView)