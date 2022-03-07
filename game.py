import pygame as pg
from random import random
X=750
Y=750
f=pg.display.set_mode(size=(X,Y))
pg.display.set_caption("Tkinter window")
fps=pg.time.Clock()
B=1

#font = pg.font.SysFont('consolas', 30)
s = pg.Surface((X,Y))  
s.set_alpha(255)
s.fill((0, 0, 0))
sign=lambda µ:abs(µ)/µ
class dep:
    x=0
    y=0
zoom=1
class Wall():
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.c=int(random()*0xffffff)
    def draw(self):
        pg.draw.rect(f,self.c,(self.x-dep.x,self.y-dep.y,self.w*zoom,self.h*zoom))
walls=[]
for i in range(50):
    walls.append(Wall(int(random()*X),
                      int(random()*Y),
                      int(random()*50),
                      int(random()*50)))
walls.append(Wall(0,0,X,10))
walls.append(Wall(0,Y-10,X,10))
walls.append(Wall(0,0,10,Y))
walls.append(Wall(X-10,0,10,Y))
walls.append(Wall(X/2-10,Y/2-10,20,20))

class Ball():
    def __init__(self):
        self.x,self.y=20,20
        self.vec=[(random()-.5)*2,(random()-.5)*2]
        self.ray=10
    def draw(self):
        pg.draw.circle(f,0xffffff,(self.x-dep.x,self.y-dep.y),self.ray)
    def move(self):
        self.x+=self.vec[0]
        self.y+=self.vec[1]
        
balle=Ball()
clavier=set()
while B:
    fps.tick(60)
    pg.display.flip()
    f.blit(s, (0, 0))
    mospos=balle.x+sign(balle.vec[0])*balle.ray,balle.y+sign(balle.vec[1])*balle.ray
    for wall in walls:
        wall.draw()
        if wall.x<mospos[0]<wall.x+wall.w and wall.y<mospos[1]<wall.y+wall.h:
            if abs(balle.x-wall.x)<balle.ray or abs(balle.x-(wall.x+wall.w))<balle.ray:
                balle.vec[0]*=-1
            else:
                balle.vec[1]*=-1
            wall.draw()
        elif abs(wall.x+wall.w/2-balle.x)<100 and abs(wall.y+wall.h/2-balle.y)<100:
            wall.draw()
    balle.draw()
    balle.move()
    for event in clavier:
        if event==pg.K_SPACE:
            balle.vec[0]*=-1
        if event==pg.K_UP:
            dep.y-=10
        if event==pg.K_DOWN:
            dep.y+=10
        if event==pg.K_LEFT:
            dep.x-=10
        if event==pg.K_RIGHT:
            dep.x+=10
        if event==pg.K_p:
            zoom+=1
        if event==pg.K_m:
            zoom-=1

        
    for event in pg.event.get():
        if event.type==pg.QUIT:
            B=0
            pg.quit()
        
        elif event.type==pg.KEYUP:
            clavier.add(event.key)
            
          
        elif event.type==pg.KEYDOWN:
            clavier=clavier.difference(set([event.key]))
            
        
