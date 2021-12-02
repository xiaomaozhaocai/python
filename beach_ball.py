import sys,pygame

pygame.init()
screen = pygame.display.set_mode([640,320])
screen.fill([255,255,255])

my_ball = pygame.image.load('beach_ball.jpg')
x,y,x_speed,y_speed = [50,50,10,10]
screen.blit(my_ball,[x,y])
pygame.display.flip()

while True:
    pygame.time.delay(20)
    pygame.draw.rect(screen, [255, 255, 255], [x, y, 50, 50], 0)
    x = x + x_speed
    y = y + y_speed
    if x > screen.get_width() - 50 or x < 0:
        x_speed = -x_speed
        
    # if x > screen.get_width():
    #     x = -50

    if y > screen.get_height() - 50 or y < 0:
        y_speed = -y_speed
    # if y > screen.get_height():
    #     y = -50

    screen.blit(my_ball, [x, y])
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()