import pygame
from ventanas.cargar_partida.clase_boton_cargar_partida import boton_cargar_partida

class ventana_cargar_partida:
    def __init__(self, ventana):
        #Define imagen de ventana
        self.ventana = ventana
        self.fondo = pygame.image.load('ventanas/menu/Fondo.png')

        #Define el tamaño de la imagen de fondo
        self.fondo = pygame.transform.scale(self.fondo, (self.ventana.get_width(), self.ventana.get_height()))

        #Carga la imagen de la base donde se colocaran los botones / Reescala imagen
        self.base = pygame.image.load('ventanas/menu/BaseMenu.png')
        self.base = pygame.transform.scale(self.base, (self.ventana.get_width()/100*50, self.ventana.get_height()/100*90))

        #POSICIONES X y Y DE LOS BOTONES
        pos_x = self.ventana.get_width() / 100 * 10         #Todos los botones estarán alineados en X
        pos_y1 = self.ventana.get_height() / 100 * 13       #Y del boton 1
        pos_y2 = self.ventana.get_height() / 100 * 32       #Y del boton 2
        pos_y3 = self.ventana.get_height() / 100 * 51       #Y del boton 3
        pos_y4 = self.ventana.get_height() / 100 * 70       #Y del boton 4

        #CREACION DE INSTANCIAS DE LOS BOTONES SEPARADOS
        self.boton1 = boton_cargar_partida(self.ventana, pos_x, pos_y1, "assets/Sprites/skeleton_Base/Idle/skeleton_Base_Idle0.png", "assets/espadas/espada_default.png" ,5, 5,"Luis miguel - Partida 1")
        self.boton2 = boton_cargar_partida(self.ventana, pos_x, pos_y2, "assets/Sprites/skeleton_Base/Idle/skeleton_Base_Idle0.png","assets/espadas/espada_default.png", 5, 5,"Andresaurio espinoza - Partida 2")
        self.boton3 = boton_cargar_partida(self.ventana, pos_x, pos_y3, "assets/Sprites/skeleton_Base/Idle/skeleton_Base_Idle0.png", "assets/espadas/espada_default.png", 5, 5,"Puñaron - Partida 3")
        self.boton4 = boton_cargar_partida(self.ventana, pos_x, pos_y4,"assets/Sprites/skeleton_Base/Idle/skeleton_Base_Idle0.png","assets/espadas/espada_default.png", 5, 5, "José José - Partida 4")

    def update(self):
        #POSICIÓN DE LA IAMGEN DE FONDO
        self.ventana.blit(self.fondo, (0,0))

        #POSICIÓN DE LA VENTANA BASE DONDE SE COLOCARÁN LOS BOTONES
        self.ventana.blit(self.base, (self.ventana.get_width()/20, self.ventana.get_height()/20))

        #REVISA SI EL MOUSE ESTÁ ENCIMA DEL MARCO DE LA IMAGEN
        self.boton1.update()
        self.boton2.update()
        self.boton3.update()
        self.boton4.update()

        #DIBUJA LAS IMAGENES DENTRO DEL LOS BOTONES
        self.boton1.draw()
        self.boton2.draw()
        self.boton3.draw()
        self.boton4.draw()