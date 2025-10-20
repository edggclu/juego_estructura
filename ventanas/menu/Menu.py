import pygame
from ventanas.menu.boton import boton


class Menu:
    def __init__(self, ventana):
        self.ventana = ventana
        self.nueva_partida = None
        self.cargar_partida = None
        self.opciones = None
        self.fondo_menu = None
        self.setup()

    def setup(self):
        self.fondo_menu = pygame.image.load("menu.jpeg")
        self.fondo_menu = pygame.transform.scale(self.fondo_menu, (self.ventana.get_width(), self.ventana.get_height()))
        self.nueva_partida = boton("Nueva Partida",self.ventana, 0)
        self.cargar_partida = boton("Cargar Partida",self.ventana, 1)
        self.opciones = boton("Opciones",self.ventana, 2)

    def update(self):
        self.ventana.blit(self.fondo_menu, (0,0))

        self.ventana.blit(self.nueva_partida.imagen, self.nueva_partida.boton_rect)
        self.ventana.blit(self.cargar_partida.imagen, self.cargar_partida.boton_rect)
        self.ventana.blit(self.opciones.imagen, self.opciones.boton_rect)

        self.ventana.blit(self.nueva_partida.texto_surface, self.nueva_partida.texto_rect)
        self.ventana.blit(self.cargar_partida.texto_surface, self.cargar_partida.texto_rect)
        self.ventana.blit(self.opciones.texto_surface, self.opciones.texto_rect)

        self.animate()
    def animate(self):
        self.nueva_partida.update()
        self.cargar_partida.update()
        self.opciones.update()

