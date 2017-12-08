#tablero ajedrez

import sys, pygame, time, math
pygame.init()

size = width, height = 800, 680 #tamaño de la pantalla
speed = [2, 2]
speed2 = [3, 3]
# Define the colors we will use in RGB format
Black = 0, 0, 0
White = (255, 255, 255)
Brown2= (89, 54, 24)
Brown = (119, 71, 26)
Gray = (216, 216, 216)
Red = (169, 0, 0)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tablero de ajedrez 3D")

X,Y=30,250 #esquina inferiror izquierda del primer cuadrito
p=50 # que tan largos serán los cuadrados (coordenada en x)
q=25 # que tan inclinados serán los cuadrados (coordenada en y)
n=q/p

######### Piezas blancas#####################
Rey1= pygame.image.load("Rey1.png").convert_alpha() #carga la imagen
Rey1Rect = Rey1.get_rect().move(X+4*p,Y-210)

Reina1= pygame.image.load("Reina1.png").convert_alpha() #carga la imagen
Reina1Rect = Reina1.get_rect().move(X+140, Y-170)

Alfil1= pygame.image.load("Alfil1.png").convert_alpha() #carga la imagen
Alfil1Rect = Alfil1.get_rect().move(X+95,Y-145)
Alfil1_1Rect = Alfil1.get_rect().move(X+5*p,Y-220)

Caballo1= pygame.image.load("Caballo1.png").convert_alpha() #carga la imagen
Caballo1Rect = Caballo1.get_rect().move(X+45,Y-110)
Caballo1_1Rect = Caballo1.get_rect().move(X+6*p-10,Y-240)

Torre1= pygame.image.load("Torre1.png").convert_alpha() #carga la imagen
Torre1Rect = Torre1.get_rect().move(X-5,Y-80)
Torre1_1Rect = Torre1.get_rect().move(X+7*p,Y-250)

Peon1= pygame.image.load("Peon1.png").convert_alpha() #carga la imagen
Peon1Rect = Peon1.get_rect().move(X+20,Y-20)
Peon2Rect = Peon1.get_rect().move(X+p+20,Y-70+q)
Peon3Rect = Peon1.get_rect().move(X+2*p+20,Y-2*p-20+ 2*q)
Peon4Rect = Peon1.get_rect().move(X+3*p+20,Y-3*p-20+ 3*q)
Peon5Rect = Peon1.get_rect().move(X+4*p+20,Y-4*p-20+ 4*q)
Peon6Rect = Peon1.get_rect().move(X+5*p+20,Y-5*p-20+ 5*q)
Peon7Rect = Peon1.get_rect().move(X+6*p+20,Y-6*p-20+ 6*q)
Peon8Rect = Peon1.get_rect().move(X+7*p+20,Y-7*p-20+ 7*q)


###########Piezas negras###########################################
Peon2= pygame.image.load("Peon2.png").convert_alpha() #carga la imagen
Peon1_1Rect = Peon2.get_rect().move(X+3*p-10,Y+5*p-q+10)
Peon2_1Rect = Peon2.get_rect().move(X+4*p-10,Y+5*p-2*q+10)
Peon3_1Rect = Peon2.get_rect().move(X+5*p-10,Y+5*p-3*q+10)
Peon4_1Rect = Peon2.get_rect().move(X+6*p-10,Y+5*p-4*q+10)
Peon5_1Rect = Peon2.get_rect().move(X+7*p-10,Y+5*p-5*q+10)
Peon6_1Rect = Peon2.get_rect().move(X+8*p-10,Y+5*p-6*q+10)
Peon7_1Rect = Peon2.get_rect().move(X+9*p-10,Y+5*p-7*q+10)
Peon8_1Rect = Peon2.get_rect().move(X+10*p-10,Y+5*p-8*q+10)

Rey2= pygame.image.load("Rey2.png").convert_alpha() #carga la imagen
Rey2Rect = Rey2.get_rect().move(488-135,415)

Reina2= pygame.image.load("Reina2.png").convert_alpha() #carga la imagen
Reina2Rect = Reina2.get_rect().move(550-149,405)

Alfil2= pygame.image.load("Alfil2.png").convert_alpha() #carga la imagen
Alfil2Rect = Alfil2.get_rect().move(425-125,460)
Alfil2_1Rect = Alfil2.get_rect().move(613-157,385)

Caballo2= pygame.image.load("Caballo2.png").convert_alpha() #carga la imagen
Caballo2Rect = Caballo2.get_rect().move(363-115,485)
Caballo2_1Rect = Caballo2.get_rect().move(675-170,365)

Torre2= pygame.image.load("Torre2.png").convert_alpha() #carga la imagen
Torre2Rect = Torre2.get_rect().move(200,520)
Torre2_1Rect = Torre2.get_rect().move(553,348)
#######################################################################


def Square(x,y,t):
    if t==0:
        pygame.draw.polygon(screen, Black, [(x,y), (x+p,y-q), (x+p-q, y-p-q), (x-q,y-p)],0)
    else:
        pygame.draw.polygon(screen, White, [(x,y), (x+p,y-q), (x+p-q, y-p-q), (x-q,y-p)],0)
        
def Board(x,y):
    a,b = x-q, y-p
    r=20
    t=25
    A=[a, b]
    B=[a+(8*p), b-(8*q)]
    C=[a + (8*q), b + 8*p]
    D=[a + 8*p +8*q, b +8*p -8*q]
    A1=[A[0]-t-8, A[1]-r]
    B1=[B[0]+r-5, B[1]-t-8]
    C1=[C[0]-r+5, C[1]+t+5]
    D1=[D[0]+t+8, D[1]+r-10]
    m=0
    for j in range(y,y+ 8*p,p):
        k=j
        for i in range(x,x+8*p,p):
            if m%2==0:
                Square(i,k,0)
            else:
                Square(i,k,1)
            k-=q
            m+=1
        x+=q
        m+=1
    ########################## Bordes
    pygame.draw.polygon(screen, Brown, [A,A1,C1,D1,D,C],0)
    pygame.draw.polygon(screen, Brown, [A,A1,B1,D1,D,B],0)        
    
                    
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

        Board(X,Y)

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
        screen.fill(Gray)
        

    pygame.quit()
