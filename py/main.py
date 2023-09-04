from math import sin, cos, radians
from pygame.draw import rect, circle, aaline
from pygame import init, quit, display, key, event, QUIT, K_UP, K_DOWN, K_RIGHT, K_LEFT

HEIGHT = 500
WIDTH = 1000

MAP = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,0,0,0,0,0,1],
    [1,0,0,0,0,0,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,1,0,0,1,1],
    [1,0,0,0,0,1,0,0,0,1],
    [1,0,0,1,0,1,1,0,0,1],
    [1,0,0,1,0,0,1,0,0,1],
    [1,0,0,1,0,0,1,0,0,1],
    [1,1,1,1,1,1,1,1,1,1],
]

L = 50
RADIUS = 10
STEPS = 1.5
ANGLES = 90
SCALE = (WIDTH/2)/ANGLES

init()
display.set_caption("raycastings")
screen = display.set_mode((WIDTH,HEIGHT))
running = True

player_x = 65
player_y = 200
player_angle = 225

def map():
    y = 0 
    for i in MAP:
        x = 0
        for j in i:
            rect(screen, "lightgray" if j == 1 else "#646464", (x,y,L,L))
            rect(screen,"black",(x,y,L,L),1)
            x += L
        del x
        y += L
    del y

def rays():
    for angle in range(ANGLES+1):
        for depth in range(int(WIDTH/2)):
            target_x = player_x - sin(radians(player_angle+angle)) * depth
            target_y = player_y + cos(radians(player_angle+angle)) * depth

            col = int(target_x / L)
            row = int(target_y / L)

            if MAP[row][col] == 1:
                rect(screen, "blue", (col * L,row * L,L-1,L-1))
                aaline(screen, "orange", (player_x, player_y), (target_x, target_y))

                color = int(255 / (1 + depth * depth * 0.0001))
                depth *= cos(radians((ANGLES/2)-angle))
                wall_height = 21000 / (depth + 0.0001)

                if wall_height > HEIGHT: wall_height = HEIGHT
                rect(screen, (color, color, color), ((WIDTH/2)+(angle*SCALE), (HEIGHT/2)-wall_height/2, SCALE, wall_height))
                break

while running:
    for Event in event.get():
        if Event.type == QUIT:
            running = False

    screen.fill("black") 

    map()
    rays()
    rect(screen, "white",(WIDTH/2,0,WIDTH/2,HEIGHT),1)

    circle(screen, "green", (player_x,player_y),RADIUS)
    
    prev_x = player_x
    prev_y = player_y
    
    angle = player_angle + (ANGLES/2)

    keys = key.get_pressed()
    if keys[K_UP]:
        player_x += -sin(radians(angle)) * STEPS
        player_y += cos(radians(angle)) * STEPS
    if keys[K_DOWN]:
        player_x -= -sin(radians(angle)) * STEPS
        player_y -= cos(radians(angle)) * STEPS
    if keys[K_RIGHT]:
        player_angle += 1
    if keys[K_LEFT]:
        player_angle -= 1

    for ang in range(0,360,45):
        a = radians(ang)
        if MAP[int((player_y-(RADIUS+.5)*sin(a))/L)][int((player_x-(RADIUS+.5)*cos(a))/L)] == 1:
            player_x = prev_x
            player_y = prev_y

    display.flip()

quit()
