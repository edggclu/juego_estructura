import pygame
from ventanas.cargar_partida.ventana_cargar_partida import ventana_cargar_partida
from ventanas.menu.Menu import Menu
from ventanas.nueva_partida.ventana_nueva_partida import ventana_nueva_partida

pygame.init()

ancho = 1080
alto = 720

estado = 'menu'
ventana = pygame.display.set_mode((ancho, alto), pygame.WINDOWMAXIMIZED)
pygame.display.set_caption("Game")

reloj = pygame.time.Clock()

# Instanciacion de Ventanas
menu = Menu(ventana)
menu_nueva_partida = ventana_nueva_partida(ventana)
cargar_menu = ventana_cargar_partida(ventana)
juego = None

run = True

while run:
    reloj.tick(60)
    if estado == 'menu':
        if menu.boton_nueva_partida.clicked:
            estado = 'ventana_nueva_partida'
        if menu.salir.clicked:
            run = False
        if menu.cargar_partida.clicked:
            estado = 'cargar'
        menu.update()
    if estado == 'ventana_nueva_partida':
        menu_nueva_partida.update()
        if menu_nueva_partida.ventana_del_juego is not None:
            juego = menu_nueva_partida.ventana_del_juego
            estado = 'juego'
    if estado == 'juego':
        juego.update()
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