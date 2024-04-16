import pygame.sprite

class GameObject(pygame.sprite.Sprite):

    def __init__(self, position, sprite, health = 1, qi_capacity = 1):
        pygame.sprite.Sprite.__init__(self)
        self.health = health
        self.qi_capcity = qi_capacity
        self.position = position
        self.rect = (position[0], position[1], 25, 25)
        self.sprite = sprite