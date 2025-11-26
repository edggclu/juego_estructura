import pygame
from ventanas.cargar_partida.ventana_cargar_partida import ventana_cargar_partida
from ventanas.menu.Menu import Menu
from ventanas.nueva_partida.ventana_nueva_partida import ventana_nueva_partida

# Inicializacion de los modulos de Pygame
pygame.init()

# Configuracion de las dimensiones y ventana principal
ancho = 1080
alto = 720

estado = 'menu'
ventana = pygame.display.set_mode((ancho, alto), pygame.WINDOWMAXIMIZED)
pygame.display.set_caption("Game")

# Control de tiempo y FPS
reloj = pygame.time.Clock()

# Instanciacion de Ventanas
menu = Menu(ventana)
menu_nueva_partida = ventana_nueva_partida(ventana)
cargar_menu = ventana_cargar_partida(ventana)
juego = None

# Configuracion de recursos graficos para el boton de regresar
btn_regresar_img = pygame.image.load('assets/Menu/BotonAtras.png')
btn_regresar_img = pygame.transform.scale(btn_regresar_img, (100, 100))
btn_regresar_rect = btn_regresar_img.get_rect()
btn_regresar_rect.x = 25
btn_regresar_rect.y = 600
mostrar_boton_regresar = False
estado_anterior = 'menu'

# Inicio del bucle principal del juego
run = True
while run:
    reloj.tick(60)

    # Logica para el estado Menu Principal
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
        mostrar_boton_regresar = False

    # Logica para el estado Nueva Partida
    if estado == 'ventana_nueva_partida':
        mostrar_boton_regresar = True
        menu_nueva_partida.update()
        if menu_nueva_partida.ventana_del_juego is not None:
            juego = menu_nueva_partida.ventana_del_juego
            estado = 'juego'

    # Logica para el estado Juego en curso
    if estado == 'juego':
        mostrar_boton_regresar = False
        juego.update()

    # Logica para el estado Cargar Partida
    if estado == 'cargar':
        mostrar_boton_regresar = True
        cargar_menu.update()

    # Manejo de eventos de cierre global excepto durante el juego
    if estado != 'juego':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    # Logica y renderizado del boton de regresar
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

    # Actualizacion de la pantalla
    pygame.display.update()

# Finalizacion de Pygame
pygame.quit()