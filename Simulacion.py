import pygame
import sys

pygame.init()

ANCHO, ALTO = 640, 480
screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Simulacion CRT")

margen = 10
display_h = int(0.8 * ALTO)
controls_h = ALTO - display_h - (margen * 2)

panel_w = (ANCHO - (3 * margen)) // 2
panel_h = (display_h - (3 * margen)) // 2

screen_size = min(panel_w, display_h - (2 * margen))

rect_lateral = pygame.Rect(margen, margen, panel_w, panel_h)
rect_superior = pygame.Rect(margen, rect_lateral.bottom + margen, panel_w, panel_h)
rect_pantalla = pygame.Rect(
    rect_lateral.right + margen,
    margen + ((display_h - screen_size) // 2),
    screen_size,
    screen_size
)
rect_controles = pygame.Rect(margen, display_h + margen, ANCHO - (2 * margen), controls_h)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fondo
    screen.fill((20, 20, 20))

    # Dibujar los 3 rectángulos
    pygame.draw.rect(screen, (255, 255, 255), rect_lateral, 2)
    pygame.draw.rect(screen, (255, 255, 255), rect_superior, 2)
    pygame.draw.rect(screen, (80, 50, 50), rect_pantalla, 2)
    pygame.draw.rect(screen, (50, 80, 80), rect_controles, 2)

    font = pygame.font.SysFont(None, 24)
    screen.blit(font.render("Vista lateral", True, (200,200,200)),
                (rect_lateral.centerx-50, rect_lateral.top+10))
    screen.blit(font.render("Vista superior", True, (200,200,200)),
                (rect_superior.centerx-50, rect_superior.top+10))
    screen.blit(font.render("Pantalla", True, (200,200,200)),
                (rect_pantalla.centerx-30, rect_pantalla.top+10))
    screen.blit(font.render("Controles", True, (200,200,200)),
                (rect_controles.centerx-40, rect_controles.top+10))

    # Actualizar ventana
    pygame.display.flip()
    clock.tick(60)  

pygame.quit()
sys.exit()