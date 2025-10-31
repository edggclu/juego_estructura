import pygame

from ventanas.cargar_partida.clase_boton_cargar_partida import boton_cargar_partida
from ventanas.menu.boton import boton


class ventana_cargar_partida:
    def __init__(self, ventana):
        self.ventana = ventana
        self.fondo = pygame.image.load('ventanas/menu/Fondo.png')
        self.fondo = pygame.transform.scale(self.fondo, (self.ventana.get_width(), self.ventana.get_height()))
        self.base = pygame.image.load('ventanas/menu/BaseMenu.png')
        self.base = pygame.transform.scale(self.base, (self.ventana.get_width()/100*50, self.ventana.get_height()/100*90))
        self.boton = boton_cargar_partida(self.ventana, "assets/Sprites/Ogre/Idle/Idle_Ogre_2.png",  "assets/espadas/espada_default.png", 5, "edgar")


    def update(self):
        self.ventana.blit(self.fondo, (0,0))
        self.ventana.blit(self.base, (self.ventana.get_width()/20, self.ventana.get_height()/20))
        self.ventana.blit(self.boton.imagen, (self.ventana.get_width()/100*10, self.ventana.get_height()/100*13))
        self.ventana.blit(self.boton.imagen, (self.ventana.get_width()/100*10, self.ventana.get_height()/100*32))
        self.ventana.blit(self.boton.imagen, (self.ventana.get_width()/100*10, self.ventana.get_height()/100*51))
        self.ventana.blit(self.boton.imagen, (self.ventana.get_width()/100*10, self.ventana.get_height()/100*70))


        self.boton.update()