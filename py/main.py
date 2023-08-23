import pygame
from operator import itemgetter

MAP = [
    [1,1,1,1,1,1,1,1],
    [1,0,1,0,0,0,0,1],
    [1,0,1,0,1,1,1,1],
    [1,0,0,0,0,1,0,1],
    [1,0,1,0,0,1,0,1],
    [1,0,1,0,0,1,0,1],
    [1,0,1,0,0,0,0,1],
    [1,1,1,1,1,1,1,1],
]

L = 40
STEPS = 4

pygame.init()
pygame.display.set_caption("title")
screen = pygame.display.set_mode((1280, 720))
running = True

player_x = 60
player_y = 60
Rects = []

def drawMap():
    Rects.clear()
    y = 0 
    for i in MAP:
        x = 0
        for j in i:
            if j == 1:
                rect = pygame.draw.rect(screen, "white", pygame.Rect(x,y,L,L),1)
                Rects.append(rect)
            x += L
        del x
        y += L
    del y

while running:
    collides = []
    
    screen.fill("black")
    drawMap()
    player = pygame.draw.circle(screen, "green", (player_x,player_y),6)
    
    collide_index = player.collidelistall(Rects)
    collide_ls = (itemgetter(*collide_index)(Rects)) if len(collide_index) > 0 else []  

    if len(collide_index) > 1:
         collides = list(collide_ls)
    elif len(collide_index) == 1:
        collides = [collide_ls]
    
    def check_stop(player_cord, cord, var):
        return (not any(player_cord == comp[cord]+var for comp in collides))
    
    stop_up = check_stop(player_y,1,40+4)
    stop_down = check_stop(player_y,1,0-4)
    stop_left = check_stop(player_x,0,40+4)
    stop_right = check_stop(player_x,0,0-4)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN] and stop_down:
            player_y += STEPS
        if keys[pygame.K_UP] and stop_up:
            player_y -= STEPS
        elif keys[pygame.K_RIGHT] and stop_right:
            player_x += STEPS
        elif keys[pygame.K_LEFT] and stop_left:
            player_x -= STEPS

    pygame.display.flip()

pygame.quit()
