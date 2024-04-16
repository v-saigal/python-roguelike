import pygame, sys, numpy, Helpers, Player


pygame.init()
clock=pygame.time.Clock()




file = "tile.png"
image = pygame.image.load(file)


screen_width = 1000
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

width_tiles = 40
height_tiles =16
map = numpy.zeros((width_tiles, height_tiles))
map_obstacles = numpy.zeros((width_tiles, height_tiles))

map_obstacles = [(5,5), (5,6), (5,7)]

player = Player.Player(numpy.zeros(2))
player_sprite = pygame.image.load(player.sprite)
helpers = Helpers.Helpers()                 
wall_sprite = pygame.image.load("wall_vertical.png")


def detect_collision(player, change, map_obstacles):
    new_pos = tuple(player.position + change)
    if new_pos in map_obstacles:
        return True
    else:
        return False

for i in range(width_tiles):
    for j in range(height_tiles):
        screen.blit(image, (i*25, j*25))
for i in map_obstacles:
    screen.blit(wall_sprite, (i[0]*25, i[1]*25))
while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            change = []
            if event.key == pygame.K_DOWN:
                change = [0, 1]
        
            if event.key == pygame.K_UP:
                change = [0, -1]
        
            if event.key == pygame.K_RIGHT:
                change = [+1, 0]

            if event.key == pygame.K_LEFT:
                change = [-1, 0]
            if change != []:
                if (detect_collision(player=player, change=change, map_obstacles=map_obstacles) == False):
                    screen.blit(image, helpers.coordinates_to_pixels(player.position))
                    player.move(change=change)


                
        screen.blit(player_sprite, helpers.coordinates_to_pixels(player.position))

        pygame.display.flip()



            