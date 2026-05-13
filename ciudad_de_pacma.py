# Crear una ciudad de hierro o parque de atraaciones usando los elementos graficos vistos con pygame (lineas, rectangulos, cuadrados, poligonos, circulos, elipses, arcos y textos) en donde los personajes son pacmanans


import pygame
import sys
import math

# Inicializamos el motor
pygame.init()

# Configuración de la pantalla (resolución de 800x600)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mi Ciudad de Hierro")

# Colores (RGB)
CIELO = (135, 206, 235)
PASTO = (34, 139, 34)
GRIS = (100, 100, 100)
ROJO = (200, 0, 0)
AMARILLO = (255, 223, 0)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
NARANJA = (255, 165, 0)

# Fuente para los letreros
font = pygame.font.SysFont("Arial", 30, bold=True)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 1. Fondo (Cielo y Pasto)
    screen.fill(CIELO)
    # Rectángulo para el suelo
    pygame.draw.rect(screen, PASTO, (0, 450, 800, 150))

    # 2. La Taquilla (Cuadrados y Rectángulos)
    # Estructura principal
    pygame.draw.rect(screen, ROJO, (50, 350, 100, 100)) # Cuadrado
    pygame.draw.rect(screen, NEGRO, (50, 350, 100, 100), 2) # Borde
    # Ventana
    pygame.draw.rect(screen, BLANCO, (75, 370, 50, 40)) 
    
    # 3. Rueda de la Fortuna (Círculos, Líneas y Elipses)
    # Base (Líneas)
    pygame.draw.line(screen, GRIS, (600, 450), (500, 250), 5)
    pygame.draw.line(screen, GRIS, (400, 450), (500, 250), 5)
    # El aro de la rueda (Círculo)
    pygame.draw.circle(screen, NEGRO, (500, 250), 150, 5)
    # El eje central
    pygame.draw.circle(screen, NARANJA, (500, 250), 10)
    # Una de las cabinas (Elipse)
    pygame.draw.ellipse(screen, AMARILLO, (475, 90, 50, 30))

    # 4. Castillo del Terror (Polígono)
    # Dibujamos un techo triangular usando polígonos
    puntos_techo = [(180, 350), (280, 250), (380, 350)]
    pygame.draw.polygon(screen, NEGRO, puntos_techo)
    pygame.draw.rect(screen, GRIS, (200, 350, 160, 100))

    # 5. Decoración: El Sol (Arco)
    # Usamos un arco para simular un destello o medio sol
    rect_arco = (650, 20, 100, 100)
    pygame.draw.arc(screen, AMARILLO, rect_arco, 0, math.pi, 5)

    # 6. Texto: El Letrero del Parque
    texto_bienvenida = font.render("CIUDAD DE HIERRO", True, NEGRO)
    screen.blit(texto_bienvenida, (200, 20))

    # Actualizar pantalla
    pygame.display.flip()