import GameObject

class Creature(GameObject.GameObject):
    def __init__(self, position, sprite):
        GameObject.GameObject.__init__(self, position, sprite)   

    def move(self, change):
        self.position = self.position + change
