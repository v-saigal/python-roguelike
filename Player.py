class Player:
    def __init__(self, position):
        self.position = position
    
    sprite = "playersprite.png"

    def move(self, change):
        self.position += change
