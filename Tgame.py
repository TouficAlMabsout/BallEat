import numpy as np
import random as rand
import time
import pygame as pg
import pygame.gfxdraw as pgg
from sys import exit

pg.init()
pg.font.init()
font = pg.font.SysFont("Engravers MT", 40)
screen = pg.display.set_mode((700,500))

class ball(object):
    def __init__(self,x,y,size=20):
        self.x=x
        self.y=y
        self.ax=1
        self.ay=1
        self.size = size
    def motion(self,mx,my,cte):
        self.ax=cte/self.size + (cte*(-self.x + mx))/self.size
        self.ay=cte/self.size + (cte*(-self.y + my))/self.size
        self.x += self.ax*cte
        self.y += self.ay*cte
    def draw(self):
        pgg.filled_circle(screen,int(self.x),int(self.y),int(self.size),(0,0,255))

class Particle(object):
    def __init__(self,x,y,size=5):
        self.x=x
        self.y=y
        self.size=size
    def draw(self):
        pgg.filled_circle(screen,int(self.x),int(self.y),self.size,(255,255,255))

def eat(ball,particle):
    if ((ball.x-particle.x)**2+(ball.y-particle.y)**2)**0.5<= ball.size+particle.size :
        return True
    return False

def touch(particle):
    if particle.size==0:
        return True
    return False       

ball1 = ball(350,250)
par_list = [Particle(rand.randint(50,650),rand.randint(50,450)) for i in range(5)]
second_list=[]
running = True
first = False
score=0

while running:            
    for event in pg.event.get() :
        if event.type == pg.QUIT :
            running = False
    screen.fill((0,0,0))
    mx , my = pg.mouse.get_pos()
    ball1.motion(mx,my,0.1)
    ball1.draw()
    text = font.render("score:"+str(score),False,(220,0,0))
    screen.blit(text,(280,10))
    for par in par_list:
            par.draw()
            if eat(ball1,par):
                par_list.remove(par)
                second_list.append(par)
                ball1.size+=0.5
                score+=10
                text = font.render("score:"+str(score),False,(220,0,0))
                screen.blit(text,(280,10))
    if len(par_list) == 0:
        score-=10
        par_list=second_list
        second_list=[]
    
  
    

            


    pg.display.update()

exit()
