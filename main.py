import pygame

from entidades.enemigo import enemigo
from entidades.jugador import jugador


pygame.init()

ancho = 800
alto = 600

mover_arriba = False
mover_abajo = False
mover_derecha = False
mover_izquierda = False

ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Game")

#Imagen de el jugador
player_image = pygame.image.load("assets/player/idle_00.png")
player_image = pygame.transform.scale(player_image, (100, 100))
jugador = jugador(50,50, player_image)

#Imagen del enemigo
enemy_image = pygame.image.load("assets/enemy/Gemini_Generated_Image_5t0q7a5t0q7a5t0q (1).png")
enemy_image = pygame.transform.scale(enemy_image, (50, 50))
slime = enemigo(100, 100, enemy_image)

reloj = pygame.time.Clock()
run = True
while run:
    reloj.tick(60)

    ventana.fill((0,0,0))

    # Calcular el evento del jugador
    delta_x = 0
    delta_y = 0

    if mover_derecha:
        delta_x = 5
    if mover_izquierda:
        delta_x = -5
    if mover_arriba:
        delta_y = -5
    if mover_abajo:
        delta_y = 5

    jugador.mover(delta_x,delta_y)
    jugador.dibujar(ventana)

    slime.seguir_jugador(jugador)
    slime.dibujar(ventana)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w: mover_arriba = True
            if event.key == pygame.K_a: mover_izquierda = True
            if event.key == pygame.K_d: mover_derecha = True
            if event.key == pygame.K_s: mover_abajo = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w: mover_arriba = False
            if event.key == pygame.K_a: mover_izquierda = False
            if event.key == pygame.K_d: mover_derecha = False
            if event.key == pygame.K_s: mover_abajo = False



    pygame.display.update()

pygame.quit()
