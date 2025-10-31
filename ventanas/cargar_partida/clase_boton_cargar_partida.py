import pygame
class boton_cargar_partida:

    def __init__(self,ventana, imagen_personaje, imagen_espada, velocidad, nombre_jugador=None):
        #textos/información del botón
        self.ventana = ventana
        self.nombre_jugaror = nombre_jugador
        self.daño_espada = 7
        self.imagen = pygame.image.load("ventanas/menu/Boton.png")
        self.boton_rect = self.imagen.get_rect()

        self.espada_default = "assets/espadas/espada_default.png"
        self.imagen_personaje = "assets/Sprites/Ogre/Idle/Idle_Ogre_2.png"
        self.velocidad = 3
        #self.imagen_personaje =

    def update(self):
        self.imagen = pygame.transform.scale(self.imagen, (360, 125))
        #self.ventana.blit(self.imagen,(0,0))