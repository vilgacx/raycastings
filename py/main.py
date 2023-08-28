from math import sin, cos, radians
import pygame

HEIGHT, WIDTH = 1000, 500 

MAP = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,0,0,0,0,0,1],
    [1,0,0,0,0,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,1,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,1,0,1,1,0,1,1],
    [1,0,0,1,0,0,1,0,0,1],
    [1,0,1,1,0,0,1,0,0,1],
    [1,1,1,1,1,1,1,1,1,1],
]

L = 50
STEPS = 1.5

pygame.init()
pygame.display.set_caption("raycastings")
screen = pygame.display.set_mode((HEIGHT,WIDTH))
running = True

player_x = 80
player_y = 200
player_angle = 225

def map():
    y = 0 
    for i in MAP:
        x = 0
        for j in i:
            pygame.draw.rect(screen, "lightgray" if j == 1 else "#646464", pygame.Rect(x,y,L,L))
            pygame.draw.rect(screen,"black",pygame.Rect(x,y,L,L),1)
            x += L
        del x
        y += L
    del y

def rays():
    for angle in range(90):
        for depth in range(WIDTH):
            target_x = player_x - sin(radians(player_angle+angle)) * depth
            target_y = player_y + cos(radians(player_angle+angle)) * depth

            col = int(target_x / L)
            row = int(target_y / L)

            if MAP[row][col] == 1:
                pygame.draw.rect(screen, "blue", (col * L,row * L,L-1,L-1))
                pygame.draw.aaline(screen, "orange", (player_x, player_y), (target_x, target_y))
                break

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    screen.fill("white")

    map()
    rays() 

    pygame.draw.circle(screen, "green", (player_x,player_y),10)
    
    prev_x = player_x
    prev_y = player_y
    
    angle = player_angle + 45

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_x += -sin(radians(angle)) * STEPS
        player_y += cos(radians(angle)) * STEPS
    if keys[pygame.K_DOWN]:
        player_x -= -sin(radians(angle)) * STEPS
        player_y -= cos(radians(angle)) * STEPS
    if keys[pygame.K_RIGHT]:
        player_angle += 1
    if keys[pygame.K_LEFT]:
        player_angle -= 1 


    if MAP[int(player_y/L)][int((player_x-10.1)/L)] == 1:
        player_x = prev_x + 0.01
        player_y = prev_y
    if MAP[int(player_y/L)][int((player_x+10.1)/L)] == 1:
        player_x = prev_x - 0.01
        player_y = prev_y
    if MAP[int((player_y-10.1)/L)][int(player_x/L)] == 1:
        player_x = prev_x
        player_y = prev_y + 0.01
    if MAP[int((player_y+10.1)/L)][int(player_x/L)] == 1:
        player_x = prev_x
        player_y = prev_y - 0.01

    for ang in range(0,360+1,45):
        a = radians(ang)
        if MAP[int((player_y-11*sin(a))/L)][int((player_x-11*cos(a))/L)] == 1:
            player_x = prev_x
            player_y = prev_y
 
    pygame.display.flip()

pygame.quit()
