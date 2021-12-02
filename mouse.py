import pygame,sys
pygame.init()
screen = pygame.display.set_mode([640,480])
backgroud = pygame.Surface(screen.get_size())
backgroud.fill([255,255,255])

clock = pygame.time.Clock()

class Ball(pygame.sprite.Sprite):
    def __init__(self,image_file,speed,location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = location
        self.speed = speed

    def move(self):
        if self.rect.left <= screen.get_rect().left or self.rect.right >= screen.get_rect().right:
            self.speed[0] = -self.speed[0]
        newpos = self.rect.move(self.speed)
        self.rect = newpos

my_ball = Ball('beach_ball.jpg',[10,0],[20,20])
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            my_ball.rect.center = event.pos

    clock.tick(30)
    screen.blit(backgroud,(0,0))
    my_ball.move()
    screen.blit(my_ball.image,my_ball.rect)
    pygame.display.flip()
