import os

import pygame

from ventanas.juego.ventana_juego import ventana_juego
from ventanas.nueva_partida.boton_eleccion_np import boton_eleccion_np
from ventanas.partida import partida


class ventana_nueva_partida:
    def __init__(self, ventana):
        self.ventana = ventana
        self.fondo = pygame.image.load('ventanas/menu/Fondo.png')
        self.fondo = pygame.transform.scale(self.fondo, (self.ventana.get_width(), self.ventana.get_height()))
        self.fase = 1
        self.armas_stats = [
                self.crear_arma("Base", 3, 3, 0),
                self.crear_arma("Blue", 1, 5, 0),
                self.crear_arma("Green", 1, 3, 1),
                self.crear_arma("Red", 5, 2, 0),
            ]

        self.lista_colores = ['Base', 'Blue', 'Green', 'Red']
        self.boton_skeleton = boton_eleccion_np(self.ventana,
                                                self.ventana.get_width()/2 - 450,
                                                self.ventana.get_height() / 2 - 400 / 2,
                                                400,400,
                                                "skeleton",
                                                'Base')
        self.boton_vampiro = boton_eleccion_np(self.ventana,
                                               self.ventana.get_width()/2 + 50,
                                               self.ventana.get_height() / 2 - 400 / 2,
                                               400,400,
                                               'vampire',
                                               'Base')
        self.botones_armas = [None, None, None, None]
        self.flecha = pygame.image.load('ventanas/nueva_partida/Flecha.png')
        self.flecha = pygame.transform.scale(self.flecha, (200,200))
        self.x_flecha = -1000
        self.y_flecha = -1000
        self.indice_boton = 0

        self.ventana_del_juego = None

        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_click = pygame.mouse.get_pressed()[0]

        self.cuadro_estadisticas_img = pygame.image.load("ventanas/menu/Cuadro.png")
        self.cuadro_estadisticas_img = pygame.transform.scale(self.cuadro_estadisticas_img, (800,350))
        self.cuadro_estadisticas_rect = pygame.rect.Rect(200,350,1050,550)

        # Texto estadisticas
        self.fuente = pygame.font.SysFont("minecraft", 30)

        self.velocidad_text = texto_stat(self.ventana, "Velocidad",self.cuadro_estadisticas_rect.x + 85,self.cuadro_estadisticas_rect.y + 40, (39, 163, 245))
        self.fuerza_txt = texto_stat(self.ventana, "Fuerza",self.velocidad_text.texto_rect.right + 110, self.velocidad_text.texto_rect.y, (204, 53, 0))
        self.curacion_txt = texto_stat(self.ventana,"Curacion", self.fuerza_txt.texto_rect.right + 110, self.fuerza_txt.y, (31, 209, 40))

    def update(self):
        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_click = pygame.mouse.get_pressed()[0]
        self.ventana.fill((0, 0, 0))
        self.ventana.blit(self.fondo, (0, 0))
        if self.fase == 1:
            self.fase_1()
        elif self.fase == 2:
            self.fase_2()

    def fase_1(self):
        self.boton_skeleton.update()
        self.boton_vampiro.update()

        if self.boton_skeleton.fondo_rect.collidepoint(self.mouse_pos):
            pygame.mouse.set_cursor(pygame.cursors.ball)
            if self.mouse_click == 1:
                pygame.mouse.set_cursor(pygame.cursors.arrow)
                self.cargar_botones_armas('skeleton')
                self.fase = 2
        elif self.boton_vampiro.fondo_rect.collidepoint(self.mouse_pos):
            pygame.mouse.set_cursor(pygame.cursors.ball)
            if self.mouse_click == 1:
                pygame.mouse.set_cursor(pygame.cursors.arrow)
                self.cargar_botones_armas('vampire')
                self.fase = 2
        else:
            pygame.mouse.set_cursor(pygame.cursors.arrow)

        self.boton_vampiro.animar()
        self.boton_skeleton.animar()

    def fase_2(self):
        for i in range(len(self.botones_armas)):
            btn = self.botones_armas[i]
            btn.update()
            if btn.fondo_rect.collidepoint(self.mouse_pos):
                pygame.mouse.set_cursor(pygame.cursors.ball)
                btn.lista_actual_sprites = btn.lista_sprites_attack
                btn.animar_bool = True
                self.x_flecha = btn.fondo_rect.x + btn.fondo_rect.width/2 - self.flecha.get_width()/2
                self.y_flecha = btn.fondo_rect.bottom - 80
                self.indice_boton = i
                btn.animar_random = False
                if btn.clicked:
                    self.nueva_partida()
            else:
                btn.animar_random = True
                pygame.mouse.set_cursor(pygame.cursors.arrow)
                btn.animar_bool = False
            self.botones_armas[self.indice_boton].animar_bool = True
        pygame.display.set_caption(f'{self.armas_stats[self.indice_boton][self.lista_colores[self.indice_boton]]["Velocidad"]}')

        self.ventana.blit(self.flecha, (self.x_flecha , self.y_flecha ))


        self.ventana.blit(self.cuadro_estadisticas_img,self.cuadro_estadisticas_rect)
        self.velocidad_text.update("VELOCIDAD", f'{self.armas_stats[self.indice_boton][self.lista_colores[self.indice_boton]]["Velocidad"]}')
        self.fuerza_txt.update("FUERZA", f'{self.armas_stats[self.indice_boton][self.lista_colores[self.indice_boton]]["Fuerza"]}')
        self.curacion_txt.update("CURACION", f'{self.armas_stats[self.indice_boton][self.lista_colores[self.indice_boton]]["Curacion"]}')

    def nueva_partida(self):
        tipo = self.botones_armas[self.indice_boton].clase_personaje
        color = self.lista_colores[self.indice_boton]
        arma = dict(self.armas_stats[self.indice_boton])
        nueva_partida = partida(f'{tipo}_{color}',
                                f'{arma}')
        self.ventana_del_juego = ventana_juego(self.ventana, nueva_partida)

    def cargar_botones_armas(self, param):
        for i in range(0, len(self.botones_armas)):
            self.botones_armas[i] = boton_eleccion_np(self.ventana,
                                                      65 + 250*i,
                                                      self.ventana.get_height() / 2 - 300,
                                                      200,200,
                                                      param,
                                                      self.lista_colores[i])
            self.botones_armas[i].animar_bool = True
            self.botones_armas[i].lista_actual_sprites = self.botones_armas[i].lista_sprites_attack
            self.botones_armas[i].offset = 16//self.armas_stats[i][self.lista_colores[i]]["Velocidad"]

        # Pone la flecha en el primer boton default
        btn = self.botones_armas[0]
        self.x_flecha = btn.fondo_rect.x + btn.fondo_rect.width / 2 - self.flecha.get_width() / 2
        self.y_flecha = btn.fondo_rect.bottom - 80

    def crear_arma(self, color, dano, velocidad, Curacion):
        arma = {
            color:{
                "Fuerza": dano,
                "Velocidad": velocidad,
                "Curacion": Curacion
        }}
        return dict(arma)

class texto_stat:
    def __init__(self,ventana, texto, x, y, color):
        self.ventana = ventana
        self.texto = texto
        self.x = x
        self.y = y
        self.color = color

        self.fuente = pygame.font.SysFont('minecraft', 30)
        self.texto_srf = self.fuente.render(self.texto, True, (255, 255, 255))
        self.texto_rect = pygame.Rect(self.x, self.y, self.texto_srf.get_width(),self.texto_srf.get_height())

        self.rectangulo_borde = pygame.Rect(self.x + self.texto_rect.width/2 - 25, self.y + 50, 60, 130)
        self.rectangulo_relleno = pygame.Rect(self.rectangulo_borde.x, self.rectangulo_borde.bottom-26, 60, 26)

    def update(self, text, valor):
        self.texto = text
        self.texto_srf = self.fuente.render(self.texto, True, (255, 255, 255))
        self.texto_rect = pygame.Rect(self.x, self.y, self.texto_srf.get_width(), self.texto_srf.get_height())
        self.ventana.blit(self.texto_srf, self.texto_rect)

        valor_srf = self.fuente.render(valor, True, (255, 255, 255))
        valor_rect = pygame.rect.Rect(self.x + self.texto_rect.width/2 - valor_srf.get_width()/2, self.y + 200,valor_srf.get_width(), valor_srf.get_height())
        self.ventana.blit(valor_srf, valor_rect)

        pygame.draw.rect(self.ventana, (self.color), self.rectangulo_borde,3)
        self.rectangulo_relleno.height = int(valor) * 26
        self.rectangulo_relleno.y = self.rectangulo_borde.bottom - int(valor) * 26
        pygame.draw.rect(self.ventana, (self.color), self.rectangulo_relleno)