import pygame

class PanelInfoBase:
    # Clase que representa el panel de información detallada de la partida.
    # Se dibuja a la derecha de la pantalla y muestra todos los datos (tiempo, dinero, kills) de
    # la partida actualmente seleccionada (hovered).

    def __init__(self, ventana, boton_info):

        #Inicializa el panel con la información

        # Parametros recibidos
        # ventana: La superficie principal de pygame
        # boton_info: La instancia de boton_cargar_partida cuya información se mostrará

        self.ventana = ventana
        self.boton = boton_info  # Referencia al objeto botón de partida

        # CARGA Y POSICIONA EL FONDO DEL PANEL
        self.panel_img = pygame.image.load('assets/Menu/BaseMenu.png').convert_alpha()
        self.panel_img = pygame.transform.scale(self.panel_img, (500, 600))
        self.panel_rect = self.panel_img.get_rect()
        # Posicionamiento: 70% del ancho y centrado verticalmente
        self.panel_rect.center = (self.ventana.get_width() * 0.70, self.ventana.get_height() / 2)

        # DEFINICIÓN DE FUENTES Y COLORES
        self.font_titulo = pygame.font.SysFont('minecraft', 40)
        self.font_stat_label = pygame.font.SysFont('minecraft', 28)
        self.font_stat_valor = pygame.font.SysFont('minecraft', 28)
        self.font_boton = pygame.font.SysFont('minecraft', 30)

        self.color_texto_label = (200, 200, 200) # Gris claro para etiquetas
        self.color_texto_valor = (255, 255, 255) # Blanco para valores importantes

        # CARGA Y ESCALADO DE ICONOS PARA ESTADÍSTICAS PRINCIPALES (COLUMNA IZQUIERDA)
        self.img_reloj = pygame.transform.scale(pygame.image.load("assets/Menu/Imagen reloj.png").convert_alpha(), (40, 40))
        self.img_dinero = pygame.transform.scale(pygame.image.load("assets/Menu/bolsaDinero.png"), (40, 40))
        self.img_espada_kills = pygame.transform.scale(pygame.image.load("assets/Menu/EspadasCruzadas.png"), (35, 35))

        # IMAGEN DEL PERSONAJE JUGADOR (Esquina Superior Izquierda del Panel)
        ruta_esqueleto = "assets/Sprites/skeleton_Base/Idle/skeleton_Base_Idle0.png"
        ruta_vampiro = "assets/Sprites/vampire_Base/Idle/sprite_0.png"
        ruta_a_cargar = ""

        # Lógica para determinar la imagen completa del personaje (con marco)
        if self.boton.ruta_imagen_personaje == ruta_esqueleto: # Si el jugador es un esqueleto
            ruta_a_cargar = "assets/Menu/Esqueleto_marco_completo.png"
        elif self.boton.ruta_imagen_personaje == ruta_vampiro: # Si el jugador es vampiro
            ruta_a_cargar = "assets/Menu/Vampiro_marco_completo.png"

        self.personaje_completo_img = pygame.transform.scale(pygame.image.load(ruta_a_cargar), (180, 180))
        self.personaje_completo_rect = self.personaje_completo_img.get_rect()
        self.personaje_completo_rect.left = self.panel_rect.left + 40  # Padding izquierdo
        self.personaje_completo_rect.top = self.panel_rect.top + 40   # Padding superior

        # CARGA Y ESCALADO DE ICONOS DE KILLS DE ENEMIGOS (COLUMNA DERECHA)
        icon_size = (80, 80)
        # Iconos Esqueletos
        self.img_skel_base = pygame.transform.scale(pygame.image.load("assets/Sprites/skeleton_Base/Idle/skeleton_Base_Idle0.png"), icon_size)
        self.img_skel_rojo = pygame.transform.scale(pygame.image.load("assets/Sprites/skeleton_Red/Idle/skeleton0.png"), icon_size)
        self.img_skel_verde = pygame.transform.scale(pygame.image.load("assets/Sprites/skeleton_Green/Idle/sprite_0.png"), icon_size)
        self.img_skel_azul = pygame.transform.scale(pygame.image.load("assets/Sprites/skeleton_Blue/Idle/sprite_0.png"), icon_size)
        # Iconos Vampiros
        self.img_vamp_base = pygame.transform.scale(pygame.image.load("assets/Sprites/vampire_Base/Idle/sprite_0.png"), icon_size)
        self.img_vamp_rojo = pygame.transform.scale(pygame.image.load("assets/Sprites/vampire_Red/Idle/sprite_0.png"), icon_size)
        self.img_vamp_verde = pygame.transform.scale(pygame.image.load("assets/Sprites/vampire_Green/Idle/sprite_0.png"), icon_size)
        self.img_vamp_azul = pygame.transform.scale(pygame.image.load("assets/Sprites/vampire_Blue/Idle/sprite_0.png"), icon_size)

        # BOTÓN DE CARGAR JUEGO
        self.boton_load_img = pygame.image.load("assets/Menu/Boton.png")
        self.boton_load_img = pygame.transform.scale(self.boton_load_img, (250, 60))
        self.boton_load_rect = self.boton_load_img.get_rect()
        self.boton_load_rect.centerx = self.panel_rect.centerx           # Centrado horizontalmente en el panel
        self.boton_load_rect.bottom = self.panel_rect.bottom - 40       # Cerca del borde inferior

        # Renderiza el texto del botón
        self.texto_load_surf = self.font_boton.render("CARGAR JUEGO", True, self.color_texto_valor)
        self.texto_load_rect = self.texto_load_surf.get_rect(center=self.boton_load_rect.center)

    def dibujar_stat_principal(self, icono, label_texto, valor_texto, y_pos):
        #Dibuja una estadística de la columna izquierda (Tiempo/Dinero).

        # Argumentos obtenidos:
        # icono: Superficie de Pygame del icono (reloj o dinero).
        # label_texto: El texto de la etiqueta (ej. "Tiempo:").
        # valor_texto: El valor numérico de la estadística.
        # y_pos: La posición Y vertical para dibujar esta fila.

        # DIBUJA EL ICONO
        icono_rect = icono.get_rect()
        icono_rect.left = self.panel_rect.left + 40  # separación izquierda
        icono_rect.top = y_pos
        self.ventana.blit(icono, icono_rect)

        # DIBUJA LA ETIQUETA ALINEADA EL ICONO
        label_surf = self.font_stat_label.render(label_texto, True, self.color_texto_label)
        label_rect = label_surf.get_rect()
        label_rect.left = icono_rect.right + 15
        label_rect.top = icono_rect.top + 3  # Alineado verticalmente con el icono
        self.ventana.blit(label_surf, label_rect)

        # DIBUJA EL VALOR DEBAJO DE LA ETIQUETA
        valor_surf = self.font_stat_valor.render(valor_texto, True, self.color_texto_valor)
        valor_rect = valor_surf.get_rect()
        valor_rect.left = label_rect.left      # Alinear con la etiqueta
        valor_rect.top = label_rect.bottom + 5 # 5px debajo de la etiqueta
        self.ventana.blit(valor_surf, valor_rect)

    def dibujar_stat_kills(self, x, y, icono, valor):

        #Dibuja una estadística de kills de enemigo (columna derecha).

        # Variables
        # x: Posición X para el icono.
        # y: Posición Y para el icono.
        # icono: Superficie de Pygame del icono del enemigo.
        # valor: El valor numérico de kills para ese enemigo.

        # DIBUJA EL ICONO
        icono_rect = icono.get_rect(topleft=(x, y))
        self.ventana.blit(icono, icono_rect)

        # DIBUJA EL TEXTO "x VALOR" (ENEMIGOS ELIMINADOS INDIVIDUALMENTE)
        texto_surf = self.font_stat_label.render(f"x {valor}", True, self.color_texto_valor)
        texto_rect = texto_surf.get_rect()

        texto_rect.left = icono_rect.right - 15   # Posicionado ligeramente a la izquierda del borde derecho del icono
        texto_rect.centery = icono_rect.centery + 15 # Centrado verticalmente, pero movido hacia abajo
        self.ventana.blit(texto_surf, texto_rect)

    def draw(self):
        #Método para dibujar todos los componentes del panel en la ventana

        # DIBUJA EL FONDO DEL PANEL
        self.ventana.blit(self.panel_img, self.panel_rect)

        # DIBUJA LA IMAGEN COMPLETA DEL PERSONAJE CON MARCO
        self.ventana.blit(self.personaje_completo_img, self.personaje_completo_rect)

        # INFORMACIÓN SUPERIOR (Nombre y Kills Totales)
        # DIBUJA EL NOMBRE DEL PERSONAJE
        nombre_surf = self.font_titulo.render(self.boton.nombre_jugador, True, self.color_texto_valor)
        nombre_rect = nombre_surf.get_rect()
        nombre_rect.left = self.personaje_completo_rect.right + 25
        nombre_rect.top = self.personaje_completo_rect.top + 10
        self.ventana.blit(nombre_surf, nombre_rect)

        # DIBUJA LAS KILLS TOTALES
        y_kills = nombre_rect.bottom + 25

        # Icono de espada izquierda
        icono_espada_izq_rect = self.img_espada_kills.get_rect()
        icono_espada_izq_rect.left = self.personaje_completo_rect.right + 25
        icono_espada_izq_rect.centery = y_kills
        self.ventana.blit(self.img_espada_kills, icono_espada_izq_rect)

        # Etiqueta "Kills:"
        kills_label_surf = self.font_stat_label.render("Kills:", True, self.color_texto_label)
        kills_label_rect = kills_label_surf.get_rect()
        kills_label_rect.left = icono_espada_izq_rect.right + 10
        kills_label_rect.centery = y_kills
        self.ventana.blit(kills_label_surf, kills_label_rect)

        # Valor de las Kills Totales
        kills_valor_surf = self.font_stat_valor.render(self.boton.enemigos_eliminados, True, self.color_texto_valor)
        kills_valor_rect = kills_valor_surf.get_rect()
        kills_valor_rect.left = kills_label_rect.right + 10
        kills_valor_rect.centery = y_kills
        self.ventana.blit(kills_valor_surf, kills_valor_rect)

        # Icono de espada derecha
        icono_espada_der_rect = self.img_espada_kills.get_rect()
        icono_espada_der_rect.left = kills_valor_rect.right + 10
        icono_espada_der_rect.centery = y_kills
        self.ventana.blit(self.img_espada_kills, icono_espada_der_rect)

        # DIBUJA LAS ESTADÍSTICAS PRINCIPALES (COLUMNA IZQUIERDA)
        y_col1 = self.personaje_completo_rect.bottom + 20  # Posición Y inicial
        espaciado_col1 = 80                               # Separación vertical
        # Tiempo
        self.dibujar_stat_principal(self.img_reloj, "Tiempo:", self.boton.tiempo_partida, y_col1)
        # Dinero
        self.dibujar_stat_principal(self.img_dinero, "Dinero:", self.boton.dinero_acumulado, y_col1 + espaciado_col1)

        # DIBUJA ESTADÍSTICAS DE KILLS POR ENEMIGO (COLUMNA DERECHA)
        x_col2_skeletons = self.personaje_completo_rect.right + 10    # Columna 1 de kills (Esqueletos)
        x_col2_vampires = x_col2_skeletons + 100                      # Columna 2 de kills (Vampiros)

        y_col2 = self.personaje_completo_rect.bottom - 90
        espaciado_col2 = 80  # Espacio vertical

        # COLUMNA DE ESQUELETOS
        self.dibujar_stat_kills(x_col2_skeletons, y_col2, self.img_skel_base, self.boton.kills_esqueleto_base)
        self.dibujar_stat_kills(x_col2_skeletons, y_col2 + espaciado_col2, self.img_skel_rojo, self.boton.kills_esqueleto_rojo)
        self.dibujar_stat_kills(x_col2_skeletons, y_col2 + espaciado_col2 * 2, self.img_skel_verde, self.boton.kills_esqueleto_verde)
        self.dibujar_stat_kills(x_col2_skeletons, y_col2 + espaciado_col2 * 3, self.img_skel_azul, self.boton.kills_esqueleto_azul)

        # COLUMNA DE VAMPIROS
        self.dibujar_stat_kills(x_col2_vampires, y_col2, self.img_vamp_base, self.boton.kills_vampiro_base)
        self.dibujar_stat_kills(x_col2_vampires, y_col2 + espaciado_col2, self.img_vamp_rojo, self.boton.kills_vampiro_rojo)
        self.dibujar_stat_kills(x_col2_vampires, y_col2 + espaciado_col2 * 2, self.img_vamp_verde, self.boton.kills_vampiro_verde)
        self.dibujar_stat_kills(x_col2_vampires, y_col2 + espaciado_col2 * 3, self.img_vamp_azul, self.boton.kills_vampiro_azul)

        # DIBUJA EL BOTON DE CARGAR PARTIDA
        self.ventana.blit(self.boton_load_img, self.boton_load_rect)
        self.ventana.blit(self.texto_load_surf, self.texto_load_rect)