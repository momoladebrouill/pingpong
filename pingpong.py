import pygame as pg
import utis
from random import random
import math

pg.init()
X=750
Y=500
f=pg.display.set_mode(size=(X+50,Y+50))
fps=pg.time.Clock()
B=1
ATTRACTION=.1
maxspeed=1
class Balle:
    def __init__(self,X,Y):
        self.x=X
        self.y=Y
        self.speed=2.5
        self.vecx=0
        self.vecy=0
        self.ray=10
        self.coul=int(random()*0xffffff)
        self.rect=pg.draw.circle(f,self.coul,(self.x,self.y),self.ray)
        
        
    def move(self):
        self.x+=self.vecx
        self.y+=self.vecy
        
    def draw(self):
        self.rect=pg.draw.circle(f,self.coul,(self.x,self.y),self.ray)
       
        
    def collide(self):
        if self.x>X:
            self.vecx=X-self.x
        elif balle.y>Y:
            self.vecy=Y-self.y
        elif self.x<0:
            self.vecx=-self.x-2
        elif self.y<0:
            self.vecy=-self.y
        else:
            ls=[]
            for obj in balls:
                if not obj is self:
                    ls.append(obj)
            who=self.rect.collidelist(ls)
     
            
            if who!=-1:
                other=balls[who]
                self.vecy+=(self.y-other.y)*ATTRACTION
                self.vecx+=(self.x-other.x)*ATTRACTION
                if self.vecx==self.vecy==0:
                    self.vecx=random()
                    self.vecy=random()
        #self.vecy+=.01
        #self.vecx-=math.copysign(.01,self.x-X/2)
        self.vecx+=(sum(obj.x for obj in balls)/len(balls)-self.x)*ATTRACTION
        self.vecy+=(sum(obj.y for obj in balls)/len(balls)-self.y)*ATTRACTION
        if self.vecx>maxspeed:self.vecx=maxspeed
        if self.vecy>maxspeed:self.vecy=maxspeed
    __repr__=lambda s:f'|{s.x},{s.y}|'
    


pres={}
def move_all(x=0,y=0):
    for balle in balls:
        balle.x+=x*10
        balle.y+=y*10
mousepos=(50,50)
balls=[Balle(X*random(),Y*random()) for _ in range(3)]
while B:
    fps.tick(60)
    pg.display.flip()
    f.fill(0)
    for balle in balls:
        balle.move()
        balle.draw()
        balle.collide()
        
    if pres.get(pg.K_z):
        move_all(0,-1)
        
    if pres.get(pg.K_q):
        move_all(-1)
        
    if pres.get(pg.K_s):
        move_all(0,1)
    if pres.get(pg.K_d):
        move_all(1)
        
    for event in pg.event.get():
        if event.type==pg.QUIT:
            B=0
            pg.quit()
        elif event.type==pg.MOUSEBUTTONUP:
            balls.append(Balle(*event.pos))
        elif event.type==pg.KEYUP:
            pres[event.dict['key']]=False
        elif event.type==pg.KEYDOWN:
            pres[event.dict['key']]=True
            
