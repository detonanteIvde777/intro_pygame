# importamos la libreria pygame

import pygame

#inicializamos los modulos de la libreria
pygame.init()

# establecer dimensiones de la ventana}
ventana = pygame.display.set_mode((400,400))

# establecer el titulo de la ventana
pygame.display.set_caption("pygame guanenta")

# definir colores
azul = ( 0,0,255)
rojo = ( 255, 0, 0)
verde = (0, 255, 0)
amarillo = (175, 255, 10)
negro = (0,0,0)

# creamos una superficie
superficie_1 = pygame.Surface((200,200))
superficie_2 = pygame.Surface((200,200))
superficie_3 = pygame.Surface((200,200))
superficie_4 = pygame.Surface((200,200))
superficie_5 = pygame.Surface((200,200))

# rellemos la superficie de color
superficie_1.fill(azul)
superficie_2.fill(rojo)
superficie_3.fill(verde)
superficie_4.fill(amarillo)
superficie_5.fill(negro)
# agregar o mover la superficie a la ventana
ventana.blit(superficie_1, (0,0))
ventana.blit(superficie_2, (200,200))
ventana.blit(superficie_3, (0,200))
ventana.blit(superficie_4, (200,0))
ventana.blit(superficie_5, (100,100))
# Actulizar visualizacion de la ventana
pygame.display.flip()

# Bucle del juego
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break

pygame.quit()