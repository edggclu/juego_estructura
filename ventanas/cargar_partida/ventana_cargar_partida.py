import pygame
from ventanas.cargar_partida.clase_boton_cargar_partida import boton_cargar_partida

class ventana_cargar_partida:
    def __init__(self, ventana):
        #Define imagen de ventana
        self.ventana = ventana
        self.fondo = pygame.image.load('assets/Menu/Fondo.png')

        # Carga la imagen de la base donde se colocaran los botones / Reescala imagen
        self.base = pygame.image.load('assets/Menu/BaseMenu.png')
        self.base = pygame.transform.scale(self.base,(self.ventana.get_width() / 100 * 50, self.ventana.get_height() / 100 * 90))

        #Posicion de la ventana donde se colocaran los botones
        self.ventana.blit(self.base, (self.ventana.get_width() / 20, self.ventana.get_height() / 20))

        #Define el tamaño de la imagen de fondo
        self.fondo = pygame.transform.scale(self.fondo, (self.ventana.get_width(), self.ventana.get_height()))



        #POSICIONES X y Y DE LOS BOTONES
        pos_x = self.ventana.get_width() / 100 * 1         #Todos los botones estarán alineados en X
        pos_y1 = self.ventana.get_height() / 100 * 13       #Y del boton 1
        pos_y2 = self.ventana.get_height() / 100 * 32       #Y del boton 2
        pos_y3 = self.ventana.get_height() / 100 * 51       #Y del boton 3
        pos_y4 = self.ventana.get_height() / 100 * 70       #Y del boton 4

        #CREACION DE INSTANCIAS DE LOS BOTONES SEPARADOS
        self.boton1 = boton_cargar_partida(self.ventana, pos_x, pos_y1, "56:06" ,"assets/Sprites/skeleton_Base/Idle/skeleton_Base_Idle0.png" ,5, 5,"Luis miguel")
        self.boton2 = boton_cargar_partida(self.ventana, pos_x, pos_y2, "56:06" ,"assets/Sprites/skeleton_Base/Idle/skeleton_Base_Idle0.png", 5, 5,"Andresaurio espinoza")
        self.boton3 = boton_cargar_partida(self.ventana, pos_x, pos_y3, "56:06" ,"assets/Sprites/skeleton_Base/Idle/skeleton_Base_Idle0.png", 5, 5,"Puñaron")
        self.boton4 = boton_cargar_partida(self.ventana, pos_x, pos_y4, "56:06" , "assets/Sprites/skeleton_Base/Idle/skeleton_Base_Idle0.png", 5, 5, "José José")
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
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def update(self):
        # Posición de la imagen de fondo
        self.ventana.blit(self.fondo, (0, 0))

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
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #MOSTRAR CUADRO DE INFORMACIÓN A LA DERECHA

        #Variable para guardar qué botón mostrar
        boton_a_mostrar = self.boton1

        #Comprueba qué botón tiene el mouse encima
        if self.boton1.hovered:
            boton_a_mostrar = self.boton1
        elif self.boton2.hovered:
            boton_a_mostrar = self.boton2
        elif self.boton3.hovered:
            boton_a_mostrar = self.boton3
        elif self.boton4.hovered:
            boton_a_mostrar = self.boton4


        #Dibuja siempre el botón
        self.ventana.blit(self.cuadro_detalles_img, self.cuadro_detalles_rect)

            # --- (AQUÍ PUEDES PONER TU CÓDIGO) ---
            # Ejemplo para mostrar el nombre del jugador de ese botón:

            # font_ejemplo = pygame.font.Font(None, 36) # Usa la fuente que quieras
            # nombre_txt = font_ejemplo.render(
            #     f"Jugador: {boton_a_mostrar.nombre_jugador}", True, (255, 255, 255)
            # )
            # # Posiciona el texto dentro del cuadro de detalles
            # self.ventana.blit(nombre_txt, (self.cuadro_detalles_rect.x + 30, self.cuadro_detalles_rect.y + 30))
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------