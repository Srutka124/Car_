



class MapManager:
    def __init__(self):
        self.model = 'block.egg'
        self.texture = 'block.png'
        self.color = (0.2 , 0.2 , 0.35 , 1)

        self.addNew()
        
    def addNew(self):
        """створення основу для новоЇ карти
        """
        self.land = render.attachNewNode('Land')
    def addBlock(self,position):
        
        cube = loader.loadModel(self.model)
        cube_texture = loader.loadTexture(self.texture)


        cube.setTexture(cube_texture)
        cube.setPos(position)
        
        cube.setColor(self.color)
        cube.reparentTo(self.land)
    def loadMap(self, filename):
         """зчитування карти """
         with open(filename) as file :
            y = 0 
            for line in file :
                x = 0
                line = line.split(" ") 
                for number in line : 
                    for z in range(int(number)+1):
                        self.addBlock((x,y,z))
                    x +=1
                y+= 1



    