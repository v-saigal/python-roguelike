import Creature

class Player(Creature.Creature):
    def __init__(self, position, sprite):
        Creature.Creature.__init__(self, position, sprite)

