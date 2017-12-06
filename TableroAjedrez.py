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

######### Piezas blancas
Rey1= pygame.image.load("Rey1.png").convert_alpha() #carga la imagen
Rey1Rect = Rey1.get_rect().move(288,35)

Reina1= pygame.image.load("Reina1.png").convert_alpha() #carga la imagen
Reina1Rect = Reina1.get_rect().move(225,75)

Alfil1= pygame.image.load("Alfil1.png").convert_alpha() #carga la imagen
Alfil1Rect = Alfil1.get_rect().move(158,100)
Alfil1_1Rect = Alfil1.get_rect().move(350,25)

Caballo1= pygame.image.load("Caballo1.png").convert_alpha() #carga la imagen
Caballo1Rect = Caballo1.get_rect().move(95,125)
Caballo1_1Rect = Caballo1.get_rect().move(413,10)

Torre1= pygame.image.load("Torre1.png").convert_alpha() #carga la imagen
Torre1Rect = Torre1.get_rect().move(30,163)
Torre1_1Rect = Torre1.get_rect().move(470, -5)

Peon1= pygame.image.load("Peon1.png").convert_alpha() #carga la imagen
Peon1Rect = Peon1.get_rect().move(75,230)
Peon2Rect = Peon1.get_rect().move(138,205)
Peon3Rect = Peon1.get_rect().move(200,180)
Peon4Rect = Peon1.get_rect().move(263,155)
Peon5Rect = Peon1.get_rect().move(325,130)
Peon6Rect = Peon1.get_rect().move(388,105)
Peon7Rect = Peon1.get_rect().move(450,80)
Peon8Rect = Peon1.get_rect().move(513,55)


###########Piezas negras
Peon2= pygame.image.load("Peon2.png").convert_alpha() #carga la imagen
Peon1_1Rect = Peon2.get_rect().move(263,480)
Peon2_1Rect = Peon2.get_rect().move(325,455)
Peon3_1Rect = Peon2.get_rect().move(388,430)
Peon4_1Rect = Peon2.get_rect().move(450,405)
Peon5_1Rect = Peon2.get_rect().move(513,380)
Peon6_1Rect = Peon2.get_rect().move(575,355)
Peon7_1Rect = Peon2.get_rect().move(638,330)
Peon8_1Rect = Peon2.get_rect().move(700,305)

Rey2= pygame.image.load("Rey2.png").convert_alpha() #carga la imagen
Rey2Rect = Rey2.get_rect().move(488,415)

Reina2= pygame.image.load("Reina2.png").convert_alpha() #carga la imagen
Reina2Rect = Reina2.get_rect().move(550,400)

Alfil2= pygame.image.load("Alfil2.png").convert_alpha() #carga la imagen
Alfil2Rect = Alfil2.get_rect().move(425,460)
Alfil2_1Rect = Alfil2.get_rect().move(613,385)

Caballo2= pygame.image.load("Caballo2.png").convert_alpha() #carga la imagen
Caballo2Rect = Caballo2.get_rect().move(363,485)
Caballo2_1Rect = Caballo2.get_rect().move(675,360)

Torre2= pygame.image.load("Torre2.png").convert_alpha() #carga la imagen
Torre2Rect = Torre2.get_rect().move(300,520)
Torre2_1Rect = Torre2.get_rect().move(738,345)

 
                    
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
        pygame.draw.polygon(screen, Black, [(313,75), (375,50), (413,100), (350,125)],0)
        pygame.draw.polygon(screen, Black, [(350,125), (288,150), (325,200), (388,175)],0)
        pygame.draw.polygon(screen, Black, [(388,175), (450,150), (488,200), (425,225)],0)
        pygame.draw.polygon(screen, Black, [(363,250), (400,300), (463,275), (425,225)],0)
        pygame.draw.polygon(screen, Black, [(463,275), (525,250), (563,300), (500,325)],0)
        pygame.draw.polygon(screen, Black, [(438,350), (475,400), (538,375), (500,325)],0)
        pygame.draw.polygon(screen, Black, [(575,425), (638,400), (600,350), (538,375)],0)
        pygame.draw.polygon(screen, Black, [(575,425), (513,450), (550,500), (613,475)],0)
        pygame.draw.polygon(screen, Black, [(638,400), (675,450), (738,425), (700,375)],0)
        pygame.draw.polygon(screen, Black, [(663,325), (725,300), (763,350), (700,375)],0)
        pygame.draw.polygon(screen, Black, [(663,325), (625,275), (563,300), (600,350)],0)
        pygame.draw.polygon(screen, Black, [(588,225), (650,200), (688,250), (625,275)],0)
        pygame.draw.polygon(screen, Black, [(488,200), (550,175), (588,225), (525,250)],0)
        pygame.draw.polygon(screen, Black, [(550,175), (613,150), (575,100), (513,125)],0)
        pygame.draw.polygon(screen, Black, [(413,100), (450,150), (513,125), (475,75)],0)
        pygame.draw.polygon(screen, Black, [(438,25), (500,0), (538,50), (475,75)],0)

        
        screen.blit(Rey1,Rey1Rect)
        screen.blit(Reina1,Reina1Rect)
        screen.blit(Alfil1,Alfil1Rect)
        screen.blit(Alfil1,Alfil1_1Rect)
        screen.blit(Caballo1,Caballo1Rect)
        screen.blit(Caballo1,Caballo1_1Rect)
        screen.blit(Torre1,Torre1Rect)
        screen.blit(Torre1,Torre1_1Rect)
        screen.blit(Peon1,Peon1Rect)
        screen.blit(Peon1,Peon2Rect)
        screen.blit(Peon1,Peon3Rect)
        screen.blit(Peon1,Peon4Rect)
        screen.blit(Peon1,Peon5Rect)
        screen.blit(Peon1,Peon6Rect)
        screen.blit(Peon1,Peon7Rect)
        screen.blit(Peon1,Peon8Rect)

        screen.blit(Peon2,Peon1_1Rect)
        screen.blit(Peon2,Peon2_1Rect)
        screen.blit(Peon2,Peon3_1Rect)
        screen.blit(Peon2,Peon4_1Rect)
        screen.blit(Peon2,Peon5_1Rect)
        screen.blit(Peon2,Peon6_1Rect)
        screen.blit(Peon2,Peon7_1Rect)
        screen.blit(Peon2,Peon8_1Rect)
        screen.blit(Rey2,Rey2Rect)
        screen.blit(Reina2,Reina2Rect)
        screen.blit(Alfil2,Alfil2Rect)
        screen.blit(Alfil2,Alfil2_1Rect)
        screen.blit(Caballo2,Caballo2Rect)
        screen.blit(Caballo2,Caballo2_1Rect)
        screen.blit(Torre2,Torre2Rect)
        screen.blit(Torre2,Torre2_1Rect)
       
        
        pygame.display.flip()
        time.sleep(.01)
        screen.fill(White)
        

    pygame.quit()
