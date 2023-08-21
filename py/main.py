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

pygame.display.set_caption("raycastingdotpy")
screen = pygame.display.set_mode((1280, 720))

L = 50

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

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()


pygame.quit()
