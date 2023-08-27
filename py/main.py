import math
import pygame

MAP = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,0,0,0,0,0,1],
    [1,0,0,1,0,1,1,1,1,1],
    [1,0,0,0,0,1,0,0,1,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,1,0,1,1,0,1,1],
    [1,0,0,1,0,0,1,0,0,1],
    [1,0,1,1,0,0,1,0,0,1],
    [1,1,1,1,1,1,1,1,1,1],
]

L = 50
STEPS = 1

pygame.init()
pygame.display.set_caption("raycastings")
screen = pygame.display.set_mode((1000,500))
running = True

player_x = 80
player_y = 200
player_angle = 225

def map():
    y = 0 
    for i in MAP:
        x = 0
        for j in i:
            pygame.draw.rect(screen, "lightgray" if j == 1 else (100, 100, 100), pygame.Rect(x,y,L,L))
            pygame.draw.rect(screen,"black",pygame.Rect(x,y,L,L),1)
            x += L
        del x
        y += L
    del y

def rays():
    for angle in range(90):
        for depth in range(500):
            target_x = player_x - math.sin(math.radians(player_angle+angle)) * depth
            target_y = player_y + math.cos(math.radians(player_angle+angle)) * depth

            col = int(target_x / L)
            row = int(target_y / L)

            if MAP[row][col] == 1:
                pygame.draw.rect(screen, "blue", (col * L,row * L,L-1,L-1))
                pygame.draw.aaline(screen, "orange", (player_x, player_y), (target_x, target_y))
                break



while running:
    screen.fill("white")

    map()
    rays()
 
    player = pygame.draw.circle(screen, "green", (player_x,player_y),10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_x += -math.sin(math.radians(player_angle + 45)) * STEPS
        player_y += math.cos(math.radians(player_angle + 45)) * STEPS
    if keys[pygame.K_DOWN]:
        player_x -= -math.sin(math.radians(player_angle + 45)) * STEPS
        player_y -= math.cos(math.radians(player_angle + 45)) * STEPS
    if keys[pygame.K_RIGHT]:
        player_angle += STEPS
    if keys[pygame.K_LEFT]:
        player_angle -= STEPS

    pygame.display.flip()

pygame.quit()
