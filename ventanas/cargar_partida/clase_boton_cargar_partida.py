import pygame
class boton_cargar_partida:

    def __init__(self,ventana, imagen_personaje, imagen_espada, velocidad, nombre_jugador=None):
        #textos/información del botón
        self.ventana = ventana
        self.nombre_jugaror = nombre_jugador
        self.daño_espada = 7
        self.ventana_boton = pygame.image.load("ventanas/menu/Boton.png")
        self.boton_rect = self.ventana_boton.get_rect()

        self.espada_default = "assets/espadas/espada_default.png"
        self.imagen_personaje = "assets/Sprites/Ogre/Idle/Idle_Ogre_2.png"
        self.velocidad = 3
        #self.imagen_personaje =

    def update(self):
        self.ventana.blit(self.ventana_boton,(0,0))