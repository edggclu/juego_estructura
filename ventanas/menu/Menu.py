import pygame
from ventanas.menu.boton import boton


class Menu:
    def __init__(self, ventana):
        self.ventana = ventana
        self.boton_nueva_partida = None
        self.cargar_partida = None
        self.opciones = None
        self.cerrar = None
        self.fondo_menu = None
        self.setup()

    def setup(self):
        self.fondo_menu = pygame.image.load("assets/Menu/Fondo.png")
        self.fondo_menu = pygame.transform.scale(self.fondo_menu, (self.ventana.get_width(), self.ventana.get_height()))
        self.boton_nueva_partida = boton("Nueva Partida", self.ventana, 0)
        self.cargar_partida = boton("Cargar Partida",self.ventana, 1)
        self.opciones = boton("Opciones",self.ventana, 2)
        self.salir = boton("Salir",self.ventana, 3)


    def update(self):
        self.ventana.blit(self.fondo_menu, (0,0))

        self.ventana.blit(self.boton_nueva_partida.imagen, self.boton_nueva_partida.boton_rect)
        self.ventana.blit(self.cargar_partida.imagen, self.cargar_partida.boton_rect)
        self.ventana.blit(self.opciones.imagen, self.opciones.boton_rect)
        self.ventana.blit(self.salir.imagen, self.salir.boton_rect)


        self.ventana.blit(self.boton_nueva_partida.texto_surface, self.boton_nueva_partida.texto_rect)
        self.ventana.blit(self.cargar_partida.texto_surface, self.cargar_partida.texto_rect)
        self.ventana.blit(self.opciones.texto_surface, self.opciones.texto_rect)
        self.ventana.blit(self.salir.texto_surface, self.salir.texto_rect)

        self.animate()
    def animate(self):
        self.boton_nueva_partida.update()
        self.cargar_partida.update()
        self.opciones.update()
        self.salir.update()

