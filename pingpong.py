import pygame as pg
from random import random
from colorsys import hsv_to_rgb
import math

from is_even import is_even as ie

ie.is_even(10)

pg.init()
X=750
Y=500
f=pg.display.set_mode(size=(X,Y))
pg.display.set_caption("Tkinter window")
fps=pg.time.Clock()
B=1

font = pg.font.SysFont('consolas', 30)
class Balle:
    def __init__(self,X,Y):
        self.x=X
        self.y=Y
        self.vecx=-10
        self.vecy=-10
        self.ray=50
        self.coul=0xfffff
        self.rect=pg.draw.rect(f,0,(self.x,self.y,self.ray,self.ray))
        
        
    def move(self):
        self.x+=self.vecx
        self.y+=self.vecy
        if self.vecx>100:
            self.vecx*=0.9
        if self.vecy>100:
            self.vecy*=0.9
        
        
    def draw(self):
        self.rect=pg.draw.rect(f,self.coul,(self.x-self.ray/2,self.y,self.ray,self.ray))
        
       
        
    def collide(self):
        if self.x>X+10:
            self.vecx=X-self.x
            d.coutdown=1
        elif balle.y>Y:
            self.vecy=Y-self.y
        elif self.x<0:
            self.vecx=-self.x
            g.coutdown=1
        elif self.y<0:
            self.vecy=-self.y
        
    __repr__=lambda s:f'|{s.x},{s.y}|'
    
class Pal:
    def __init__(self,x,y,fac):
        self.x=x;
        self.y=y;
        self.fac=fac;
        self.coul=0xffffff;
        self.height=100
        self.coutdown=0
        self.rect=pg.draw.rect(f,self.coul,(self.x,self.y,10,self.height))
        
    def move(self):
        self.y+=(balle.y-(self.y+self.height/2))/self.fac
        
    def draw(self):
        if self.coutdown:
            self.coutdown+=1
            f.blit(text,(balle.x-chocolat.width/2,balle.y-chocolat.height*2))
            truc=int(self.coutdown/60*255)
            self.coul=0xff0000+truc*255+truc
            if self.coutdown==30:
                self.coul=0xffffff
                self.coutdown=0
        self.rect=pg.draw.rect(f,self.coul,(self.x,self.y,10,self.height))
       
    

pres={}
mousepos=(50,50)
balle=Balle(X/2,Y/2)
s = pg.Surface((X,Y))  
s.set_alpha(255)
s.fill((0, 0, 0))
g=Pal(0,0,7)
d=Pal(X-10,0,20)
text = font.render("#@!%", False, (255,255,255),0)
chocolat=text.get_rect()
while B:
    fps.tick(60)
    pg.display.flip()
    f.blit(s, (0, 0))
    
    
    balle.move()
    balle.draw()
    balle.collide()
    g.move()
    g.draw()
    d.move()
    d.draw()
        
    if pres.get(pg.K_UP):
        balle.vecy+=-1
        
    if pres.get(pg.K_DOWN):
        balle.vecy+=1
   
        
        

        
    for event in pg.event.get():
        if event.type==pg.QUIT:
            B=0
            pg.quit()
        elif event.type==pg.KEYUP:
            if event.key==pg.K_SPACE:
                balle.vecy*=-1
                
            pres[event.dict['key']]=False
        elif event.type==pg.KEYDOWN:
            pres[event.dict['key']]=True
            
