import pygame
from ventanas.cargar_partida.clase_boton_cargar_partida import boton_cargar_partida
from ventanas.cargar_partida.PanelInfoBase import PanelInfoBase

class ventana_cargar_partida:
    def __init__(self, ventana):
        #Define imagen de ventana
        self.ventana = ventana
        self.fondo = pygame.image.load('assets/Menu/Fondo.png')

        #Define el tamaño de la imagen de fondo
        self.fondo = pygame.transform.scale(self.fondo, (self.ventana.get_width(), self.ventana.get_height()))

        #POSICIONES X y Y DE LOS BOTONES
        pos_x = self.ventana.get_width() / 100 * 1         #Todos los botones estarán alineados en X
        pos_y1 = self.ventana.get_height() / 100 * 13       #Y del boton 1
        pos_y2 = self.ventana.get_height() / 100 * 32       #Y del boton 2
        pos_y3 = self.ventana.get_height() / 100 * 51       #Y del boton 3
        pos_y4 = self.ventana.get_height() / 100 * 70       #Y del boton 4

        #CREACION DE INSTANCIAS DE LOS BOTONES SEPARADOS
        self.boton1 = boton_cargar_partida(self.ventana, pos_x, pos_y1, 21 ,"assets/Sprites/vampire_Base/Idle/sprite_0.png" ,"Luis miguel")
        self.boton2 = boton_cargar_partida(self.ventana, pos_x, pos_y2, 17 ,"assets/Sprites/skeleton_Base/Idle/skeleton_Base_Idle0.png", "Andresaurio espinoza")
        self.boton3 = boton_cargar_partida(self.ventana, pos_x, pos_y3, 55 ,"assets/Sprites/skeleton_Base/Idle/skeleton_Base_Idle0.png", "Puñaron")
        self.boton4 = boton_cargar_partida(self.ventana, pos_x, pos_y4, 12 ,"assets/Sprites/skeleton_Base/Idle/skeleton_Base_Idle0.png",  "José José")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #CREACIÓN DE CUADRO CON INFORMACIÓN A LA DERECHA

        #CARGA LA IMAGEN
        self.cuadro_detalles_img = pygame.image.load('assets/Menu/BaseMenu.png')

        #ESCALA LA IMAGEN
        self.cuadro_detalles_img = pygame.transform.scale(self.cuadro_detalles_img, (500, 600))

        #CREA EL RECT DE LA IMAGEN
        self.cuadro_detalles_rect = self.cuadro_detalles_img.get_rect()

        #POSICIONA EL CUADRO
        self.cuadro_detalles_rect.center = (self.ventana.get_width() * 0.70, self.ventana.get_height() / 2)

        #SE ESTABLECE EL BOTÓN 1 COMO LA INFORMACIÓN POR DEFECTO (PARA ACTUALIZAR LA INFORMACIÓN DEL CUADRO GRANDE)
        self.boton_info_actual = self.boton1
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def update(self):
        # Posición de la imagen de fondo
        self.ventana.blit(self.fondo, (0, 0))

        # REVISA SI EL MOUSE ESTÁ ENCIMA DEL MARCO DE LA IMAGEN
        self.boton1.update()
        self.boton2.update()
        self.boton3.update()
        self.boton4.update()

        # --- ¡CAMBIO IMPORTANTE 2! ---
        # 3. Actualizamos cuál es el botón "activo" SI el mouse está encima de uno.
        # Si no está encima de ninguno, 'self.boton_info_actual' no cambia.
        if self.boton1.hovered:
            self.boton_info_actual = self.boton1
        elif self.boton2.hovered:
            self.boton_info_actual = self.boton2
        elif self.boton3.hovered:
            self.boton_info_actual = self.boton3
        elif self.boton4.hovered:
            self.boton_info_actual = self.boton4
        # --- Fin del cambio ---

        #DIBUJA LAS IMAGENES DENTRO DEL LOS BOTONES
        self.boton1.draw()
        self.boton2.draw()
        self.boton3.draw()
        self.boton4.draw()

        #Dibuja el cuadro con la información (usando la nueva lógica)
        self.Recuadro_informacion()


    def Recuadro_informacion(self):
        panel_detalles = PanelInfoBase(self.ventana, self.boton_info_actual)
        panel_detalles.draw()