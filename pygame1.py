import sys, pygame, time
pygame.init()

size = width, height = 1300, 700 #tamaño de la pantalla
speed = [2, 2]
speed2 = [3, 3]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ping pong")

ball = pygame.image.load("ball.png").convert_alpha() #carga la imagen
ballrect = ball.get_rect().move(50,50)
ball2 = pygame.image.load("ball.png") #carga la imagen
ballrect2 = ball2.get_rect().move(500,600)


time.sleep(5)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed) #pelota 1
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    ballrect2 = ballrect2.move(speed2) #pelota 2
    if ballrect2.left < 0 or ballrect2.right > width:
        speed2[0] = -speed2[0]
    if ballrect2.top < 0 or ballrect2.bottom > height:
        speed2[1] = -speed2[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    screen.blit(ball2, ballrect2)
    pygame.display.flip()
