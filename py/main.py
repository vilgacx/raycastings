import pygame

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
STEPS = 2

pygame.init()
pygame.display.set_caption("title")
screen = pygame.display.set_mode((1280, 720))
running = True

player_x = (L * 1) + 20
player_y = (L * 1) + 20

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
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_DOWN]:
            player_y += STEPS
        elif keys[pygame.K_UP]:
            player_y -= STEPS
        elif keys[pygame.K_RIGHT]:
            player_x += STEPS
        elif keys[pygame.K_LEFT]:
            player_x -= STEPS

    drawMap()
    player = pygame.draw.circle(screen, "green", (player_x,player_y),10)
    #player.collidelistall(Rects)
    
    pygame.display.flip()

pygame.quit()
