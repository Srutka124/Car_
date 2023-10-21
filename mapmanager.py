class MapManager:
    def __init__(self):
        self.model = 'model/block/block.egg'
        self.texture = 'model/block/block.png'
        self.color = (0.2, 0.2, 0.35, 0.5)# 4 прозорість

        self.addNew() #create new location

    def addNew(self):
        """створюєм основну для нової карти
        """
        self.land = render.attachNewNode('Land')
        
    def addBlock(self, position):
        """створює блок
        """

        block = loader.loadModel(self.model)
        block_texture = loader.loadTexture(self.texture)


        block.setTexture(block_texture)
        block.setPos(position)
        block.setColor(self.color)
        block.reparentTo(self.land)

    def loadMap(self, filename):
        """зчитування карти
        """
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(" ")
                for number in line:
                    for z in range(int(number) + 1):
                        self.addBlock((x,y,z))
                    x +=1
                y +=1
