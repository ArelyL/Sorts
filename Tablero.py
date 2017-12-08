#tablero ajedrez

import sys, pygame, time
pygame.init()

size = width, height = 1000, 650 #tamaño de la pantalla
speed = [2, 2]
speed2 = [3, 3]
# Define the colors we will use in RGB format
Black = 0, 0, 0
White = (255, 255, 255)
Brown2= (89, 54, 24)
Brown = (119, 71, 26)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tablero de ajedrez 3D")
 
                    
if __name__=='__main__':

    done = False
    clock = pygame.time.Clock()

    while not done:
        # This limits the while loop to a max of 10 times per second.
        # Leave this out and we will use all CPU we can.
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True

        ######################## Bordes
        pygame.draw.polygon(screen, Brown, [(300,600), (295,618), (824,407), (800,400)],0)
        pygame.draw.polygon(screen, Brown, [(519,0), (500,0), (800,400), (824,407)],0)
        pygame.draw.polygon(screen, Brown, [(0,200), (0,225), (295,618), (300,600)],0)
        pygame.draw.polygon(screen, Brown, [(0,184), (0,200), (500,0), (460,0)],0)

        ######################## Base
        pygame.draw.polygon(screen, Brown2, [(0,225), (0,260), (295,653), (295,618)],0)
        pygame.draw.polygon(screen, Brown2, [(295,618), (295,653), (824,442), (824,407)],0)


         ######################## Cuadros
        pygame.draw.polygon(screen, Black, [(63,175), (125,150), (163,200), (100,225)],0)
        pygame.draw.polygon(screen, Black, [(38,250), (75,300), (138,275), (100,225)],0)
        pygame.draw.polygon(screen, Black, [(138,275), (175,325), (238,300), (200,250)],0)
        pygame.draw.polygon(screen, Black, [(113,350), (175,325), (213,375), (150,400)],0)
        pygame.draw.polygon(screen, Black, [(275,350), (213,375), (250,425), (313,400)],0)
        pygame.draw.polygon(screen, Black, [(188,450), (225,500), (288,475), (250,425)],0)
        pygame.draw.polygon(screen, Black, [(288,475), (350,450), (388,500), (325,525)],0)
        pygame.draw.polygon(screen, Black, [(263,550), (325,525), (363,575), (300,600)],0)
        pygame.draw.polygon(screen, Black, [(188,125), (225,175), (288,150), (250,100)],0)
        pygame.draw.polygon(screen, Black, [(200,250), (263,225), (225,175), (163,200)],0)
        pygame.draw.polygon(screen, Black, [(300,275), (363,250), (325,200), (263,225)],0)
        pygame.draw.polygon(screen, Black, [(300,275), (238,300), (275,350), (338,325)],0)
        pygame.draw.polygon(screen, Black, [(313,400), (375,375), (413,425), (350,450)],0)
        pygame.draw.polygon(screen, Black, [(388,500), (450,475), (488,525), (425,550)],0)
        pygame.draw.polygon(screen, Black, [(450,475), (513,450), (475,400), (413,425)],0)
        pygame.draw.polygon(screen, Black, [(400,300), (338,325), (375,375), (438,350)],0)
##        pygame.draw.polygon(screen, Black, [(), (), (), ()],0)
##        pygame.draw.polygon(screen, Black, [(), (), (), ()],0)
##        pygame.draw.polygon(screen, Black, [(), (), (), ()],0)
##        pygame.draw.polygon(screen, Black, [(), (), (), ()],0)
        

       
        
        pygame.display.flip()
        time.sleep(.01)
        screen.fill(White)

    pygame.quit()
