import pygame
import sys
import math

# --- CONSTANTES Y CONFIGURACIÓN ---
# Usamos mayúsculas para constantes globales (PEP 8)
WIDTH, HEIGHT = 400, 400
FPS = 60

# Paleta de colores (Tuplas constantes)
COLORS = {
    "BLACK":   (0, 0, 0),
    "WHITE":   (255, 255, 255),
    "RED":     (255, 0, 0),
    "BLUE":    (0, 0, 255),
    "ORANGE":  (255, 165, 0),
    "GREEN":   (0, 255, 0),
    "PINK":    (255, 192, 203),
    "YELLOW":  (255, 255, 0),
    "CYAN":    (0, 255, 255)
}

def init_game():
    """Inicializa los módulos de Pygame y la ventana."""
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Optimización de Formas y Texto")
    return screen

def draw_shapes(surface):
    """Encapsula toda la lógica de dibujo."""
    pi = math.pi

    # Líneas de fondo
    pygame.draw.line(surface, COLORS["RED"], (0, 0), (400, 400), 5)
    pygame.draw.line(surface, COLORS["RED"], (0, 400), (400, 0), 5)

    # Polilíneas
    pts_1 = [(0, 0), (50, 100), (100, 50), (250, 200), (400, 400)]
    pts_2 = [(200, 0), (400, 200), (200, 400), (0, 200)]
    pygame.draw.lines(surface, COLORS["BLUE"], False, pts_1, 2)
    pygame.draw.lines(surface, COLORS["ORANGE"], True, pts_2, 2)

    # Rectángulos
    pygame.draw.rect(surface, COLORS["PINK"], (150, 150, 50, 50))
    pygame.draw.rect(surface, COLORS["GREEN"], (200, 200, 50, 50), 3)

    # Polígonos (Estrella y Rombo)
    puntos_estrella = [(200,50),(240,150),(350,150),(260,220),(300,340),
                       (200,270),(100,340),(140,220),(50,150),(160,150)]
    pygame.draw.polygon(surface, COLORS["CYAN"], puntos_estrella, 3)

    # Curvas y Círculos
    pygame.draw.circle(surface, COLORS["WHITE"], (300, 300), 100)
    pygame.draw.ellipse(surface, COLORS["ORANGE"], (200, 250, 200, 100), 3)
    pygame.draw.arc(surface, COLORS["CYAN"], (200, 0, 200, 200), pi/4, 7*pi/4, 5)

def main():
    screen = init_game()
    clock = pygame.time.Clock()
    
    # OPTIMIZACIÓN: La fuente se carga UNA SOLA VEZ fuera del bucle
    try:
        font_arial = pygame.font.SysFont("Arial", 35, bold=True)
    except:
        font_arial = pygame.font.Font(None, 35) # Fallback si Arial no existe
        
    text_surface = font_arial.render("dotonanteIvde777", True, COLORS["WHITE"])

    running = True
    while running:
        # 1. Gestión de Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 2. Actualización de Lógica (aquí irían movimientos si los hubiera)

        # 3. Renderizado
        screen.fill(COLORS["BLACK"])
        
        draw_shapes(screen)
        screen.blit(text_surface, (10, 50)) # Dibujamos el texto pre-renderizado

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()