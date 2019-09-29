import pygame,sys,random
from pygame.color import THECOLORS
import math

pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
# for i in range(100):
#     width = random.randint(0, 250)
#     height = random.randint(0,100)
#     top = random.randint(0,400)
#     left = random.randint(0,500)
#     print(THECOLORS.keys())
#     color_name = random.choice(THECOLORS.keys()())
#     print(color_name)
#     color = THECOLORS[color_name]
#     pygame.draw.rect(screen,color,[left,top,width,height],0)

# pygame.draw.circle(screen,THECOLORS['purple2'],[320,240],30,0)
# pygame.draw.rect(screen,THECOLORS['lightskyblue1'],[320,240,30,30],2)
plotPoints = []
for x in range(640):
    y = int(math.sin(x/640 * 4 * math.pi) * 200 + 240)
    plotPoints.append([x,y])
    # pygame.draw.rect(screen,[0,0,0],[x,y,1,1],1)

pygame.draw.lines(screen,[0,0,0],False,plotPoints,2)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
