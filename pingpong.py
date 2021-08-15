import pygame as pg
import utis
from utis import math

pg.init()
X=750
Y=500
f=pg.display.set_mode(size=(X,Y))
fps=pg.time.Clock()
B=1
class balle:
    x=X/2
    y=Y/2
    ray=5
    vec=utis.Vec(long=5,angle=math.tau/6)
    rect=pg.draw.circle(f,0xffffff,(x,y),ray)
    def frwd():
        balle.x+=balle.vec.x
        balle.y+=balle.vec.y
    def mv():
        balle.frwd()
        balle.draw()
        palets=[gauche,droite]
        ind=balle.rect.collidelist(palets)
        if ind!=-1:
            truc=palets[ind]
            if balle.y<truc.y:
                balle.vec.collide(math.pi/2)
                balle.frwd()
            elif balle.y>truc.y:
                balle.vec.collide(math.pi/2)
                balle.frwd()
            else:
                balle.vec.collide(math.pi)
                balle.frwd()
            
            
        if balle.x>X or balle.x<0:
            balle.vec.collide(math.pi/2)
            balle.frwd()
        if balle.y>Y or balle.y<0:
            balle.vec.collide(math.pi)
            balle.frwd()
    def draw():
        balle.rect=pg.draw.circle(f,0xffffff,(balle.x,balle.y),balle.ray)

class Pal:
    def __init__(self):
        self.x=10
        self.y=Y/2
        self.rect=pg.Rect(self.x,self.y,10,50)
    def draw(self):
        self.rect=pg.draw.rect(f,0xff0000,(self.x,self.y,10,50))
pres={}
gauche=Pal()
droite=Pal()
droite.x=X-gauche.x-10
while B:
    fps.tick(60)
    pg.display.flip()
    f.fill(0)
    balle.mv()
    balle.draw()
    gauche.draw()
    droite.draw()
    if pres.get(pg.K_a):
        gauche.y-=10
    elif pres.get(pg.K_q):
        gauche.y+=10
    if pres.get(pg.K_p):
        droite.y-=10
    elif pres.get(pg.K_m):
        droite.y+=10
    droite.y=droite.y%Y
    gauche.y=gauche.y%Y
    for event in pg.event.get():
        if event.type==pg.QUIT:
            B=0
            pg.quit()
        elif event.type==pg.KEYUP:
            pres[event.dict['key']]=False
        elif event.type==pg.KEYDOWN:
            pres[event.dict['key']]=True
            
