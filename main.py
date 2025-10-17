import pygame
from entidades.enemigo import enemigo
from entidades.jugador import jugador
from  mapa import Map

pygame.init()

ancho = 800
alto = 600

ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Game")

#Imagen de el jugador
jugador = jugador(50, 50, ventana, "assets/skeleton/idle/idle_00.png")

#Imagen del enemigo
enemy_image = pygame.image.load("assets/enemy/Gemini_Generated_Image_5t0q7a5t0q7a5t0q (1).png")
enemy_image = pygame.transform.scale(enemy_image, (50, 50))
slime = enemigo(100, 100, enemy_image)

reloj = pygame.time.Clock()
run = True

mapa_juego = Map("assets/mapa/mi_mapa.tmx")
fondo_mapa = mapa_juego.crear_mapa()
while run:
    reloj.tick(60)

    ventana.fill((0,0,0))

    ventana.blit(fondo_mapa, (0, 0))

    jugador.update()

    slime.seguir_jugador(jugador)
    slime.dibujar(ventana)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            jugador.key_down(event)
        if event.type == pygame.KEYUP:
            jugador.key_up(event)

    pygame.display.update()

pygame.quit()
