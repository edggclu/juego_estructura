import pygame

class PanelInfoBase:
    def __init__(self, ventana, boton_info):
        self.ventana = ventana
        self.boton = boton_info  # Esta es la instancia del botón con toda la información

        #CARGA EL PANEL DE FONDO
        self.panel_img = pygame.image.load('assets/Menu/BaseMenu.png').convert_alpha()
        self.panel_img = pygame.transform.scale(self.panel_img, (500, 600))
        self.panel_rect = self.panel_img.get_rect()
        self.panel_rect.center = (self.ventana.get_width() * 0.70, self.ventana.get_height() / 2)

        #DEFINE FUENTES
        self.font_titulo = pygame.font.SysFont('minecraft', 40)
        self.font_stat_label = pygame.font.SysFont('minecraft', 28)
        self.font_stat_valor = pygame.font.SysFont('minecraft', 28)
        self.font_boton = pygame.font.SysFont('minecraft', 30)

        self.color_texto_label = (200, 200, 200)
        self.color_texto_valor = (255, 255, 255)

        #CARGA LOS ICONOS PARA LAS ESTADÍSTICAS (COLUMNA IZQUIERDA)
        self.img_reloj = pygame.transform.scale(pygame.image.load("assets/Menu/Imagen reloj.png").convert_alpha(), (40, 40))
        self.img_dinero = pygame.transform.scale(pygame.image.load("assets/Menu/bolsaDinero.png"), (40, 40))
        self.img_espada_kills = pygame.transform.scale(pygame.image.load("assets/Menu/EspadasCruzadas.png"), (35, 35))

        #IMAGEN DEL PERSONAJE JUGADOR (ESQUINA SUPERIOR IZQUIERDA)
        ruta_esqueleto = "assets/Sprites/skeleton_Base/Idle/skeleton_Base_Idle0.png"
        ruta_vampiro = "assets/Sprites/vampire_Base/Idle/sprite_0.png"

        # Lógica para cargar la imagen completa
        if self.boton.ruta_imagen_personaje == ruta_esqueleto:              #Si el jugador es un esqueleto
            ruta_a_cargar = "assets/Menu/Esqueleto_marco_completo.png"
        if self.boton.ruta_imagen_personaje == ruta_vampiro:                #Si el jugador es vampiro
            ruta_a_cargar = "assets/Menu/Vampiro_marco_completo.png"

        self.personaje_completo_img = pygame.transform.scale(pygame.image.load(ruta_a_cargar), (180, 180))
        self.personaje_completo_rect = self.personaje_completo_img.get_rect()
        self.personaje_completo_rect.left = self.panel_rect.left + 40  # Padding izquierdo
        self.personaje_completo_rect.top = self.panel_rect.top + 40  # Padding superior

        #CARGA ICONOS DE KILLS DE ENEMIGOS (COLUMNA DERECHA)
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

        #BOTÓN DE CARGAR JUEGO
        self.boton_load_img = pygame.image.load("assets/Menu/Boton.png")
        self.boton_load_img = pygame.transform.scale(self.boton_load_img, (250, 60))
        self.boton_load_rect = self.boton_load_img.get_rect()
        self.boton_load_rect.centerx = self.panel_rect.centerx
        self.boton_load_rect.bottom = self.panel_rect.bottom - 40

        self.texto_load_surf = self.font_boton.render("CARGAR JUEGO", True, self.color_texto_valor)
        self.texto_load_rect = self.texto_load_surf.get_rect(center=self.boton_load_rect.center)

    def dibujar_stat_principal(self, icono, label_texto, valor_texto, y_pos):
        #DIBUJA LA LINEA DE ESTADISTICAS (ICONO, ETIQUETA, VALOR) PARA LA COLUMNA IZQUIERDA (TIEMPO Y DINERO)
        icono_rect = icono.get_rect()
        icono_rect.left = self.panel_rect.left + 40  # Padding izquierdo del icono
        icono_rect.top = y_pos
        self.ventana.blit(icono, icono_rect)

        #DIBUJA LA ETIQUETA (alineada al icono)
        label_surf = self.font_stat_label.render(label_texto, True, self.color_texto_label)
        label_rect = label_surf.get_rect()
        label_rect.left = icono_rect.right + 15
        label_rect.top = icono_rect.top + 3  # Alineado verticalmente
        self.ventana.blit(label_surf, label_rect)

        #DIBUJA EL VALOR (debajo de la etiqueta)
        valor_surf = self.font_stat_valor.render(valor_texto, True, self.color_texto_valor)
        valor_rect = valor_surf.get_rect()
        valor_rect.left = label_rect.left  # Alinear con la etiqueta
        valor_rect.top = label_rect.bottom + 5  # 5px debajo de la etiqueta
        self.ventana.blit(valor_surf, valor_rect)

    def dibujar_stat_kills(self, x, y, icono, valor):
        #Dibuja las estadísticas de Kills (Icono, valor de kills) para la columna derecha (Kills de enemigos).
        #DIBUJA EL ICONO
        icono_rect = icono.get_rect(topleft=(x, y))
        self.ventana.blit(icono, icono_rect)

        #DIBUJA EL TEXTO
        texto_surf = self.font_stat_label.render(f"x {valor}", True, self.color_texto_valor)
        texto_rect = texto_surf.get_rect()

        texto_rect.left = icono_rect.right -15
        texto_rect.centery = icono_rect.centery +15
        self.ventana.blit(texto_surf, texto_rect)

    def draw(self):
        #DIBUJA EL FONDO DEL PANEL
        self.ventana.blit(self.panel_img, self.panel_rect)

        #DIBUJA LA IMAGEN COMPLETA (MARCO MAS PERSONAJE)
        self.ventana.blit(self.personaje_completo_img, self.personaje_completo_rect)

        #DIBUJA EL NOMBRE DEL PERSONAJE
        nombre_surf = self.font_titulo.render(self.boton.nombre_jugador, True, self.color_texto_valor)
        nombre_rect = nombre_surf.get_rect()
        nombre_rect.left = self.personaje_completo_rect.right + 25
        nombre_rect.top = self.personaje_completo_rect.top + 10
        self.ventana.blit(nombre_surf, nombre_rect)

        #DIBUJA LAS KILLS TOTALES
        y_kills = nombre_rect.bottom + 25
        icono_espada_izq_rect = self.img_espada_kills.get_rect()
        icono_espada_izq_rect.left = self.personaje_completo_rect.right + 25
        icono_espada_izq_rect.centery = y_kills
        self.ventana.blit(self.img_espada_kills, icono_espada_izq_rect)

        kills_label_surf = self.font_stat_label.render("Kills:", True, self.color_texto_label)
        kills_label_rect = kills_label_surf.get_rect()
        kills_label_rect.left = icono_espada_izq_rect.right + 10
        kills_label_rect.centery = y_kills
        self.ventana.blit(kills_label_surf, kills_label_rect)

        kills_valor_surf = self.font_stat_valor.render(self.boton.enemigos_eliminados, True, self.color_texto_valor)
        kills_valor_rect = kills_valor_surf.get_rect()
        kills_valor_rect.left = kills_label_rect.right + 10
        kills_valor_rect.centery = y_kills
        self.ventana.blit(kills_valor_surf, kills_valor_rect)

        icono_espada_der_rect = self.img_espada_kills.get_rect()
        icono_espada_der_rect.left = kills_valor_rect.right + 10
        icono_espada_der_rect.centery = y_kills
        self.ventana.blit(self.img_espada_kills, icono_espada_der_rect)

        #DIBUJA LAS ESTADÍSTICAS (COLUMNA IZQUIERDA) ---
        y_col1 = self.personaje_completo_rect.bottom +20  # Mueve en general la columna de la izquierda de las estadisticas (Arriba/Abajo)
        espaciado_col1 = 80                               # Separación vertical que hay entre las estadísticas
        self.dibujar_stat_principal(self.img_reloj, "Tiempo:",self.boton.tiempo_partida, y_col1)
        self.dibujar_stat_principal(self.img_dinero, "Dinero:", self.boton.dinero_acumulado, y_col1 + espaciado_col1)

        #DIBUJA ESTADÍSTICAS DE KILLS (COLUMNA DERECHA)
        x_col2_skeletons = self.personaje_completo_rect.right + 10   #Mueve en general todos los cuadros de enemigos y kills hacia la izquierda/derecha
        x_col2_vampires = x_col2_skeletons + 100  # Espacio horizontal para la 2da columna de kills

        y_col2 = self.personaje_completo_rect.bottom -90
        espaciado_col2 = 80  # Espacio vertical entre cada icono de kill

        #COLUMNA DE ESQUELETOS
        self.dibujar_stat_kills(x_col2_skeletons, y_col2, self.img_skel_base, self.boton.kills_esqueleto_base)
        self.dibujar_stat_kills(x_col2_skeletons, y_col2 + espaciado_col2, self.img_skel_rojo,self.boton.kills_esqueleto_rojo)
        self.dibujar_stat_kills(x_col2_skeletons, y_col2 + espaciado_col2 * 2, self.img_skel_verde,self.boton.kills_esqueleto_verde)
        self.dibujar_stat_kills(x_col2_skeletons, y_col2 + espaciado_col2 * 3, self.img_skel_azul,self.boton.kills_esqueleto_azul)

        #COLUMNA DE VAMPIROS
        self.dibujar_stat_kills(x_col2_vampires, y_col2, self.img_vamp_base, self.boton.kills_vampiro_base)
        self.dibujar_stat_kills(x_col2_vampires, y_col2 + espaciado_col2, self.img_vamp_rojo,self.boton.kills_vampiro_rojo)
        self.dibujar_stat_kills(x_col2_vampires, y_col2 + espaciado_col2 * 2, self.img_vamp_verde,self.boton.kills_vampiro_verde)
        self.dibujar_stat_kills(x_col2_vampires, y_col2 + espaciado_col2 * 3, self.img_vamp_azul,self.boton.kills_vampiro_azul)

        #DIBUJA EL BOTON DE CARGAR PARTIDA
        self.ventana.blit(self.boton_load_img, self.boton_load_rect)
        self.ventana.blit(self.texto_load_surf, self.texto_load_rect)