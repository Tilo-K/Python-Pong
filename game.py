# Pong Game
# Author: Tilo K
# Github: https://github.com/Tilo-K
# DevPyVersion: 3.6.1
import pygame
from random import randint
import time

global fps
fps = 60

class Player():
    def __init__(self, x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = 1
        self.up = False
        self.down = False
    def update(self):
        if self.up == True:
            self.y -= self.speed

        if self.down == True:
            self.y += self.speed
    
        if self.y + self.h - dimensions[1] > 0:
            self.y = dimensions[1] - self.h


        if self.y < 0:
            self.y = 0
        #print('[Updated] Y: ' + str(self.y) + ' UP: ' + str(self.up) + ' DOWN: ' + str(self.down))
        self.x = int(self.x)
        self.y = int(self.y)

    def setSpeed(self, n):
        self.speed = n


class Ball():
    def __init__(self,x,y,r):
        self.x = int(x)
        self.y = int(y)
        self.r = int(r)
        self.velx = 0
        self.vely = 0
        
    def update(self):
        self.x += self.velx
        self.y += self.vely

        self.x = int(self.x)
        self.y = int(self.y)

    def setVel(self, x, y):
        self.velx = int(x)
        self.vely = int(y)
        
def ai(p, b, speed):
    if p.y+p.h/2 > b.y:
        p.y -= speed
        p.y = int(p.y)
    elif p.y+p.h/2 < b.y:
        p.y += speed
        p.y = int(p.y)



def check(p1, p2, ball):
    if ball.x-40 <= p1.x:
        if ball.y in range(p1.y, p1.y+p1.h):
            ball.setVel(ball.velx * -1, int(randint(-5,5)))  
                
    if ball.x+15 >= p2.x:
        #print('-----------')
        #print(ball.y)
        #print(p2.y)
        if ball.y in range(p2.y, p2.y+p2.h):
            ball.setVel(ball.velx * -1, int(randint(-5,5)))

    if ball.y+15 >= dimensions[1]:
        ball.setVel(ball.velx, -2.5)

    if ball.y-15 <= 0:
        ball.setVel(ball.velx, 2.5)


def checkPoint(ball):
    global pointsPA
    global pointsPB
    
    if ball.x+15 >= dimensions[0]:
        pointsPA += 1
        ball.x = int(dimensions[0] /2)
        ball.y = int(dimensions[1] /2)
        ball.setVel(0,0)
        pygame.display.update()
        time.sleep(3)
        ball.setVel(randint(1,5),randint(1,5))
    elif ball.x-15 <= 0:
        pointsPB += 1
        ball.x = int(dimensions[0] /2)
        ball.y = int(dimensions[1] /2)
        ball.setVel(0,0)
        pygame.display.update()
        time.sleep(3)
        ball.setVel(randint(1,5),randint(1,5))


pygame.init()

myfont = pygame.font.SysFont("arial", 40)


dimensions = (640, 480)

# Colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode(dimensions)
pygame.display.set_caption('Pong - Tilo K')

clock = pygame.time.Clock()

# Game variables
global pointsPA
global pointsPB

pointsPA = 0
pointsPB = 0
win = False

p = Player(10,0,25,100)
pai = Player(dimensions[0] - 35, 0, 25, 100)
ball = Ball(dimensions[0] / 2, dimensions[1] / 2, 15)

p.setSpeed(10)
ball.setVel(5,0)
while not win:
    if pointsPA >= 10:
        win = True
    elif pointsPB >= 10:
        win = True
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            win = True

        # KeyPressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                p.down = True
            if event.key == pygame.K_UP:
                p.up = True

            if event.key == pygame.K_o:
                fps += 1

            if event.key == pygame.K_l:
                fps -= 1
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                p.down = False
            if event.key == pygame.K_UP:
                p.up = False
        
    # has to beat first !!!!!!!!!!!!!!!!
    gameDisplay.fill(white)
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    p.update()
    ball.update()
    ai(pai, ball, 3)
    check(p, pai, ball)
    checkPoint(ball)

    pygame.draw.rect(gameDisplay, black, (p.x,p.y,p.w,p.h), 0)
    pygame.draw.rect(gameDisplay, blue, (pai.x,pai.y,pai.w,pai.h), 0)
    pygame.draw.circle(gameDisplay, red, (ball.x,ball.y), ball.r, 0)

    # render text
    label = myfont.render(str(pointsPA) + " | " + str(pointsPB), 1, (0,0,0))
    gameDisplay.blit(label, (dimensions[0]/2-40, 25))
    
    pygame.display.update()

    clock.tick(fps)
    #print(fps)


# end
pygame.quit()
quit()
