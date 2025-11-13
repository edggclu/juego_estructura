from ventanas.cargar_partida.clase_boton_cargar_partida import boton_cargar_partida
import pygame

class PanelInfoBase:
    def __init__(self, ventana, boton_info):
        self.ventana = ventana
        self.boton = boton_info  # Esta es la instancia del botón con toda la información

        #CARGA Y CONFIGURA EL PANEL DE FONDO
        self.panel_img = pygame.image.load('assets/Menu/BaseMenu.png').convert_alpha()    #Carga la imagen
        self.panel_img = pygame.transform.scale(self.panel_img, (500, 600))          #Escala el panel

        # Posiciona el panel a la derecha
        self.panel_rect = self.panel_img.get_rect()
        self.panel_rect.center = (self.ventana.get_width() * 0.70, self.ventana.get_height() / 2)  # Ajusta este 0.70 si se requiere más a la derecha o izquierda

        #Define la fuente de texto
        self.font_titulo = pygame.font.SysFont('minecraft', 40)
        self.font_stat_label = pygame.font.SysFont('minecraft', 28)
        self.font_stat_valor = pygame.font.SysFont('minecraft', 28, )

        self.color_texto_label = (200, 200, 200)  # Un color más suave para etiquetas
        self.color_texto_valor = (255, 255, 255)  # Blanco brillante para valores

        #CARGA ICONOS PARA LAS ESTADISTICAS
        self.img_reloj = self.cargar_icono("assets/Menu/Imagen reloj.png", (40, 40))                    #Reloj
        self.img_dinero = self.cargar_icono("assets/Menu/bolsaDinero.png", (40, 40))                    #Bolsa dinero
        self.img_espada = self.cargar_icono("assets/Menu/EspadasCruzadas.png", (40, 40))                #Espada
        self.img_enemigos = self.cargar_icono("assets/Sprites/skeleton_Base/Idle/skeleton_Base_Idle0.png", (40, 40))

        #Imagen personaje
        self.personaje_img = self.boton.imagen_personaje                                         #Carga la imagen del personaje
        self.personaje_img_grande = pygame.transform.scale(self.personaje_img, (180, 180))  #La escalamos
        self.personaje_rect = self.personaje_img_grande.get_rect()                               #Se obtiene el rect

        # Posicionamos la imagen del personaje
        self.personaje_rect.left = self.panel_rect.left + 40
        self.personaje_rect.top = self.panel_rect.top + 40

    def cargar_icono(self, ruta, tamano=(40, 40)):
        img = pygame.image.load(ruta).convert_alpha()
        return pygame.transform.scale(img, tamano)

    def dibujar_stat(self, icono, label_texto, valor_texto, y_pos):

        # Posición del Icono
        icono_rect = icono.get_rect()
        icono_rect.left = self.panel_rect.left + 40  # Padding izquierdo fijo
        icono_rect.top = y_pos
        self.ventana.blit(icono, icono_rect)

        #Posición de la Etiqueta "Tiempo:"
        label_surf = self.font_stat_label.render(label_texto, True, self.color_texto_label)
        label_rect = label_surf.get_rect()

        label_rect.left = icono_rect.right + 50
        label_rect.centery = icono_rect.centery
        self.ventana.blit(label_surf, label_rect)

        #Posición del Valor "56:06"
        valor_surf = self.font_stat_valor.render(valor_texto, True, self.color_texto_valor)
        valor_rect = valor_surf.get_rect()
        valor_rect.right = self.panel_rect.right - 30  # Alineado a la derecha
        valor_rect.centery = icono_rect.centery
        self.ventana.blit(valor_surf, valor_rect)

    def draw(self):
        # 1. Dibuja el fondo del panel
        self.ventana.blit(self.panel_img, self.panel_rect)

        # 2. Dibuja la imagen grande del personaje
        self.ventana.blit(self.personaje_img_grande, self.personaje_rect)

        # 3. Dibuja el nombre del jugador
        nombre_surf = self.font_titulo.render(self.boton.nombre_jugador, True, self.color_texto_valor)
        nombre_rect = nombre_surf.get_rect()

        nombre_rect.centerx = self.panel_rect.centerx
        nombre_rect.top = self.personaje_rect.bottom + 15

        self.ventana.blit(nombre_surf, nombre_rect)

        # 4. Dibuja todas las estadísticas
        # Define la posición Y inicial y el espaciado
        y_inicial = nombre_rect.top + self.font_titulo.get_linesize() + 40
        espaciado = 60  # Espacio vertical entre cada estadística

        # Usamos los atributos de la instancia 'self.boton' que recibimos
        self.dibujar_stat(self.img_reloj, "Tiempo:", self.boton.tiempo_partida, y_inicial)
        self.dibujar_stat(self.img_dinero, "Dinero:", self.boton.dinero_acumulado, y_inicial + espaciado)
        self.dibujar_stat(self.img_espada, "Velocidad:", self.boton.velocidad_espada, y_inicial + espaciado * 2)
        self.dibujar_stat(self.img_enemigos, "Enemigos:", self.boton.enemigos_eliminados, y_inicial + espaciado * 3)