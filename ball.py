import pygame
class Ball:
    #pass
   #class variables
   RADIUS=10


   def __init__(self,x,y,vx,vy,screen, wcolor,bgcolor, CONSTS):
       #intance variables
       self.x = x
       self.y = y
       self.vx = vx
       self.vy = vy
       self.screen=screen
       self.wcolor=wcolor
       self.bgcolor=bgcolor
       self.CONSTS = CONSTS

   def show(self, color):
       pygame.draw.circle(self.screen, color,(self.x,self.y), self.RADIUS) 
  
   def update(self):
       # new position=op+dp
       #delete old ball
       self.show(self.bgcolor)
       px = self.x + self.vx
       py = self.y + self.vy
       
       #check if collision with wall
       #left wall
       if px<(self.CONSTS.BORDER + self.RADIUS):
           self.vx=-self.vx
       
       #Top and bottom wall
       if py<(self.CONSTS.BORDER + self.RADIUS) or py>(self.CONSTS.HEIGHT - self.CONSTS.BORDER - self.RADIUS):
               self.vy=-self.vy
       
           
           

       self.x = self.x + self.vx
       self.y = self.y + self.vy
       self.show(self.wcolor)
    #    pass
   
   

    



