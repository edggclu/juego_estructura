import pygame
from pygame import Surface

from entidades.enemigo import enemigo
from entidades.jugador import jugador
from  mapa import Map
from ventanas.menu.Menu import Menu

pygame.init()

ancho = 800
alto = 600

ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Game")

#Imagen de el jugador
jugador = jugador(50, 50, ventana, "Skeleton1")

#Imagen del enemigo
enemy_image = pygame.image.load("assets/enemy/Gemini_Generated_Image_5t0q7a5t0q7a5t0q (1).png")
enemy_image = pygame.transform.scale(enemy_image, (50, 50))
slime = enemigo(100, 100, enemy_image)

reloj = pygame.time.Clock()

mapa_juego = Map("assets/mapa/mi_mapa.tmx")
fondo_mapa = mapa_juego.crear_mapa()



def jugando():
    ventana.fill((0, 0, 0))

    ventana.blit(fondo_mapa, (0, 0))

    jugador.update()
    # slime.seguir_jugador(jugador)
    slime.dibujar(ventana)

estado = 'menu'
menu = Menu(ventana)
run = True
while run:
    reloj.tick(60)
    if estado == 'jugando':
        jugando()
    if estado == 'menu':
        menu.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            jugador.key_down(event)
        if event.type == pygame.KEYUP:
            jugador.key_up(event)

    pygame.display.update()

pygame.quit()

