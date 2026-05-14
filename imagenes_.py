import pygame, sys

pygame.init()

pantalla = pygame.display.set_mode((378,442))
pygame.display.set_caption("Mario bros")
negro = (0,0,0)
pantalla.fill(negro)

# cargar imagenes
mario = pygame.image.load("assets/imagenes/mario03.png").convert()
# ubicar la imagen de la ventana
pantalla.blit(mario, (5,5))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.flip()