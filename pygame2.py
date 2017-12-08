import sys, pygame, time
pygame.init()

size = width, height = 1000, 650 #tamaño de la pantalla
speed = [2, 2]
speed2 = [3, 3]
# Define the colors we will use in RGB format
black = 0, 0, 0
WHITE = (255, 255, 255)
BLUE =  (0, 0, 89)
GREEN = (0, 100, 0)
RED =   (169, 0, 0)
Pink =  (255,   102,   102)
Purple = (148, 0, 89)
Yellow = (237, 237, 2)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("3D")

##########punto de fuga########################
x_0, y_0 = width/2, 0

############funcion#############################
def Three_point(x, y, z):
    #offset para y 
    y_1 = (height - 150) - y
  
    #calculo de y nueva
    y = y_1 - 1
   
    #offset para x
    x_1 = width/2 + x
 
    ###########ecuacion de la recta#######################33
    if y_1==0:
        m=0
    else:
        m=1.0*((y - y_1))/(-y_1) #pendiente
     
    x= x_1 + (x_0 - x_1)*m
    
    if abs(x)-abs(int(x))>0.5:
        x=int(x)+1
    else:
        x=int(x)
   #####################################################33
    print x, y
    return [x, y]       
                    
if __name__=='__main__':
    #puntos a converger
    P=[0,0]
    P_1=[-500,0]
    P_2=[500,0]
    P_3=[200,-100]
    P_4=[-300,100]

    #puntos del triángulo
    P1=[-50,0]
    P2=[50,0]
    P3=[0,75]
    
    done = False
    clock = pygame.time.Clock()

    z=0
    while not done:
        pygame.draw.circle(screen,RED, [width/2,0], 5, 0) ##punto de fuga
        # This limits the while loop to a max of 10 times per second.
        # Leave this out and we will use all CPU we can.
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True

        P=Three_point(P[0], P[1],z)
        P_1=Three_point(P_1[0], P_1[1],z)
        P_2=Three_point(P_2[0], P_2[1],z)
        P_3=Three_point(P_3[0], P_3[1],z)
        P_4=Three_point(P_4[0], P_4[1],z)

        
        pygame.draw.circle(screen,GREEN, P, 5, 0)
        pygame.draw.circle(screen,BLUE, P_1, 5, 0)
        pygame.draw.circle(screen,Purple, P_2, 5, 0)
        pygame.draw.circle(screen,Pink, P_3, 5, 0)
        pygame.draw.circle(screen,Yellow, P_4, 5, 0)
        
        P=[P[0]- width/2, (height - 150) - P[1]]
        P_1=[P_1[0]- width/2, (height - 150) - P_1[1]]
        P_2=[P_2[0]- width/2, (height - 150) - P_2[1]]
        P_3=[P_3[0]- width/2, (height - 150) - P_3[1]]
        P_4=[P_4[0]- width/2, (height - 150) - P_4[1]]

        ##############Triangulo###########################
        P1=Three_point(P1[0], P1[1],z)
        P2=Three_point(P2[0], P2[1],z)
        P3=Three_point(P3[0], P3[1],z)

        pygame.draw.polygon(screen,WHITE,[P1,P2,P3],5)

        P1=[P1[0]- width/2, (height - 150) - P1[1]]
        P2=[P2[0]- width/2, (height - 150) - P2[1]]
        P3=[P3[0]- width/2, (height - 150) - P3[1]]
        ####################################################
        
        z+=1
        if z==max(P[1], P_1[1], P_2[1], P_3[1], P_4[1]):#500:
            done=True
        
        pygame.display.flip()
        time.sleep(.01)
        screen.fill(black)

    pygame.quit()
