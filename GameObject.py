import pygame.sprite, pygame, Helpers

class GameObject(pygame.sprite.Sprite):

    def __init__(self, position, sprite, health = 1, qi_capacity = 1, helpers="h"):
        pygame.sprite.Sprite.__init__(self)
        self.health = health
        self.qi_capcity = qi_capacity
        self.helpers = Helpers.Helpers()
        self.position_pixels = self.helpers.coordinates_to_pixels(position)
        self.position = position
        self.rect = pygame.Rect(position[0], position[1], 25, 25)
        self.image = sprite

    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, value):
        print(value)
        self._position = value
        self.position_pixels = self.helpers.coordinates_to_pixels(value)


    
        