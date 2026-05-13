import pygame
import sys
import math

# Inicializamos el motor
pygame.init()

# Configuración de la pantalla (resolución de 800x600)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mi Ciudad de Hierro con Pac-Mans")

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

def dibujar_pacman(superficie, x, y, radio):
    # Cuerpo del Pac-Man (un arco relleno)
    # El ángulo va de 30 a 330 grados para dejar la boca abierta
    rect = (x - radio, y - radio, radio * 2, radio * 2)
    inicio_angulo = math.radians(30)
    fin_angulo = math.radians(330)
    
    # Dibujamos varios arcos para rellenarlo (ya que draw.arc no rellena)
    # O usamos un círculo y un polígono negro para la boca
    pygame.draw.circle(superficie, AMARILLO, (x, y), radio)
    puntos_boca = [(x, y), (x + radio, y - radio//1.5), (x + radio, y + radio//1.5)]
    pygame.draw.polygon(superficie, PASTO if y > 450 else CIELO, puntos_boca) 
    
    # Ojo
    pygame.draw.circle(superficie, NEGRO, (x + radio//4, y - radio//2), radio//6)

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
    pygame.draw.rect(screen, ROJO, (50, 350, 100, 100)) 
    pygame.draw.rect(screen, NEGRO, (50, 350, 100, 100), 2) 
    pygame.draw.rect(screen, BLANCO, (75, 370, 50, 40)) 
    
    # 3. Rueda de la Fortuna (Círculos, Líneas y Elipses)
    pygame.draw.line(screen, GRIS, (600, 450), (500, 250), 5)
    pygame.draw.line(screen, GRIS, (400, 450), (500, 250), 5)
    pygame.draw.circle(screen, NEGRO, (500, 250), 150, 5)
    pygame.draw.circle(screen, NARANJA, (500, 250), 10)
    pygame.draw.ellipse(screen, AMARILLO, (475, 90, 50, 30))

    # 4. Castillo del Terror (Polígono)
    puntos_techo = [(180, 350), (280, 250), (380, 350)]
    pygame.draw.polygon(screen, NEGRO, puntos_techo)
    pygame.draw.rect(screen, GRIS, (200, 350, 160, 100))

    # 5. Decoración: El Sol (Arco)
    rect_arco = (650, 20, 100, 100)
    pygame.draw.arc(screen, AMARILLO, rect_arco, 0, math.pi, 5)

    # 6. Texto: El Letrero del Parque
    texto_bienvenida = font.render("detonanteIvde777", True, NEGRO)
    screen.blit(texto_bienvenida, (200, 20))

    # --- AGREGANDO LOS TRES MINI PAC-MANS ---
    
    # Pac-Man 1: En el pasto (cerca de la taquilla)
    dibujar_pacman(screen, 120, 520, 20)
    
    # Pac-Man 2: En el cielo (como si volara)
    dibujar_pacman(screen, 700, 150, 15)
    
    # Pac-Man 3: Cerca del castillo
    dibujar_pacman(screen, 400, 400, 12)

    # Actualizar pantalla
    pygame.display.flip()