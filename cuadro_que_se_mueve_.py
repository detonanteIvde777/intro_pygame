# importamos la libreria pygame
import pygame
import sys

# inicializamos los modulos de la librería
pygame.init()

# Establecer dimensiones de la ventana
ventana = pygame.display.set_mode((400,400))

# establecer titulo de la ventana
pygame.display.set_caption("Rebotes rectángulo")

# definición colores
rojo = (255,0,0)
azul = (0,0,255)

# variable de movimiento
XX = 300
MOVIMIENTO = 3

# Objeto para la gestión del tiempo
clock = pygame.time.Clock()


# bucle principal del juego
while True:
    # Maximo de fotogramas por segundo
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ventana.fill(azul)

    # movimiento del rectángulo
    XX = XX + MOVIMIENTO

    if XX >= 320:
        XX = 320
        MOVIMIENTO = -3
    elif XX <= 0:
        XX = 0
        MOVIMIENTO = 3

    # dibujar rectangulo en ventana
    pygame.draw.rect(ventana, rojo, (XX,100,80,80))

    # actualizar visualización de la ventana
    pygame.display.flip()
