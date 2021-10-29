from ball import Ball
from paddle import Paddle
from collections import namedtuple
import pygame
import random

def main():
    pygame.init()

    pygame.display.set_caption("Lab2")

    WIDTH=800
    HEIGHT=480
    VELOCITY=10
    BORDER=20
    FPS = 30 #framerate


    Constants = namedtuple("Constants",["WIDTH","HEIGHT","BORDER", "VELOCITY", "FPS"])
    CONSTS=Constants(WIDTH,HEIGHT,BORDER,VELOCITY,FPS)
    screen=pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.update()

    #walls
    wcolor=pygame.Color("white")
    bgcolor=pygame.Color("black")
   
    #upper wall
    # Rect((left,top),(width,height))
    pygame.draw.rect(screen,wcolor,pygame.Rect((0,0),(WIDTH,BORDER)))

    #left wall
    pygame.draw.rect(screen,wcolor,pygame.Rect((0,0),(BORDER,HEIGHT)))

    #bottom wall
    pygame.draw.rect(screen,wcolor,pygame.Rect((0,HEIGHT-BORDER),(WIDTH,BORDER)))

    #ball init
    x0=WIDTH - Ball.RADIUS
    y0=HEIGHT//2
    vx0=-VELOCITY
    vy0=random.randint(-VELOCITY, VELOCITY)
    b0 = Ball(x0,y0,vx0,vy0,screen,wcolor,bgcolor, CONSTS)
    b0.show(wcolor)

    pygame.display.update()


    # define a variable to control the main loop
    running=True
    clock = pygame.time.Clock()

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        pygame.display.update()
        clock.tick(FPS)

        b0.update()
            

             
     

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()