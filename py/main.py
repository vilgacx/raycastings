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

pygame.init()
pygame.display.set_caption("title")
screen = pygame.display.set_mode((1280, 720))
running = True

L = 50

player_x = 60
player_y = 60


def drawMap():
    y = 0
    for i in MAP:
        x = 0
        for j in i:
            if j == 1:
                pygame.draw.rect(screen, "white", pygame.Rect(x,y,L,L),1)
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
            player_y += 5
        elif keys[pygame.K_UP]:
            player_y -= 5
        elif keys[pygame.K_RIGHT]:
            player_x += 5
        elif keys[pygame.K_LEFT]:
            player_x -= 5
    drawMap()
    pygame.draw.circle(screen, "green", (player_x,player_y),10)
    pygame.display.flip()

pygame.quit()
