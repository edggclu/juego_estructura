import pygame
from ventanas.cargar_partida.ventana_cargar_partida import ventana_cargar_partida
from ventanas.menu.Menu import Menu
from ventanas.juego.ventana_juego import ventana_juego

pygame.init()

ancho = 1080
alto = 720

estado = 'menu'
ventana = pygame.display.set_mode((ancho, alto), pygame.WINDOWMAXIMIZED)
pygame.display.set_caption("Game")

reloj = pygame.time.Clock()

menu = Menu(ventana)
juego = ventana_juego(ventana)
cargar_menu = ventana_cargar_partida(ventana)

run = True

while run:
    reloj.tick(60)
    if estado == 'jugando':
        juego.update()
    if estado == 'menu':
        if menu.nueva_partida.clicked:
            estado = 'jugando'
        if menu.salir.clicked:
            run = False
        if menu.cargar_partida.clicked:
            estado = 'cargar'
        menu.update()
    if estado == 'cargar':
        cargar_menu.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            juego.jugador.key_down(event)
        if event.type == pygame.KEYUP:
            juego.jugador.key_up(event)

    pygame.display.update()

pygame.quit()