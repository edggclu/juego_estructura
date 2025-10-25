import pygame

from ventanas.cargar_partida.clase_boton_cargar_partida import boton_cargar_partida
from ventanas.menu.boton import boton


class ventana_cargar_partida:
    def __init__(self, ventana):
        self.ventana = ventana
        self.fondo = pygame.image.load('ventanas/menu/Fondo.png')
        self.fondo = pygame.transform.scale(self.fondo, (ventana.get_width(), ventana.get_height()))
        self.base = pygame.image.load('ventanas/menu/BaseMenu.png')
        self.base = pygame.transform.scale(self.base, (800,600))
        self.boton = boton_cargar_partida(self.ventana, "assets/Sprites/Ogre/Idle/Idle_Ogre_2.png",  "assets/espadas/espada_default.png", 5, "edgar")



    def update(self):
        self.ventana.blit(self.fondo, (0,0))
        self.ventana.blit(self.base, (0,0))
        self.boton.update()