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

btn_regresar_img = pygame.image.load('ventanas/menu/BotonAtras.png')
btn_regresar_img = pygame.transform.scale(btn_regresar_img, (100,100))
btn_regresar_rect = btn_regresar_img.get_rect()
btn_regresar_rect.x = 25
btn_regresar_rect.y = 600
mostrar_boton_regresar = False
estado_anterior = 'menu'

run = True
while run:
    reloj.tick(60)
    if estado == 'menu':
        if menu.boton_nueva_partida.clicked:
            menu.boton_nueva_partida.clicked = False
            estado = 'ventana_nueva_partida'
        if menu.salir.clicked:
            menu.salir.clicked = False
            run = False
        if menu.cargar_partida.clicked:
            menu.cargar_partida.clicked = False
            estado = 'cargar'
        menu.update()
    if estado == 'ventana_nueva_partida':
        mostrar_boton_regresar = True
        menu_nueva_partida.update()
        if menu_nueva_partida.ventana_del_juego is not None:
            juego = menu_nueva_partida.ventana_del_juego
            estado = 'juego'
    if estado == 'juego':
        mostrar_boton_regresar = False
        juego.update()
    if estado == 'cargar':
        mostrar_boton_regresar = True
        cargar_menu.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if estado == 'juego':
            if event.type == pygame.KEYDOWN:
                juego.jugador.key_down(event)
            if event.type == pygame.KEYUP:
                juego.jugador.key_up(event)

    if mostrar_boton_regresar:
        if btn_regresar_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] == 1:
                if estado == 'cargar':
                    estado = 'menu'
                if estado == 'ventana_nueva_partida':
                    if menu_nueva_partida.fase == 2:
                        menu_nueva_partida.fase = 1
                    else:
                        estado = 'menu'
        ventana.blit(btn_regresar_img, btn_regresar_rect)
    pygame.display.update()

pygame.quit()