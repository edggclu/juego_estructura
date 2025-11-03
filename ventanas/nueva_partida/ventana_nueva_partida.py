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
        self.x_flecha = 0
        self.y_flecha = 0
        self.indice_boton = 0

        self.ventana_del_juego = None

    def update(self):
        self.ventana.fill((0, 0, 0))
        self.ventana.blit(self.fondo, (0, 0))
        if self.fase == 1:
            self.fase_1()
        elif self.fase == 2:
            self.fase_2()

    def fase_1(self):
        self.boton_skeleton.update()
        self.boton_vampiro.update()

        if self.boton_skeleton.hover or self.boton_vampiro.hover:
            pygame.mouse.set_cursor(pygame.cursors.ball)
        else:
            pygame.mouse.set_cursor(pygame.cursors.arrow)

        if self.boton_skeleton.clicked:
            pygame.mouse.set_cursor(pygame.cursors.arrow)
            self.cargar_botones_armas('skeleton')
            self.fase = 2
        if self.boton_vampiro.clicked:
            pygame.mouse.set_cursor(pygame.cursors.arrow)
            self.cargar_botones_armas('vampire')
            self.fase = 2


        self.boton_vampiro.animar()
        self.boton_skeleton.animar()

    def fase_2(self):
        for i in range(len(self.botones_armas)):
            btn = self.botones_armas[i]
            btn.update()
            if btn.hover:
                btn.lista_actual_sprites = btn.lista_sprites_attack
                btn.animar_bool = True
                self.x_flecha = btn.fondo_rect.x + btn.fondo_rect.width/2 - self.flecha.get_width()/2
                self.y_flecha = btn.fondo_rect.bottom - 80
                self.indice_boton = i
                if btn.clicked:
                    self.nueva_partida()
            else:
                btn.animar_bool = False
            self.botones_armas[self.indice_boton].animar_bool = True
        pygame.display.set_caption(f'{self.botones_armas[self.indice_boton].clase_personaje}_{self.lista_colores[self.indice_boton]}')



        self.ventana.blit(self.flecha, (self.x_flecha , self.y_flecha ))


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
            self.botones_armas[i].animar_bool = False
            self.botones_armas[i].offset = 1

    def crear_arma(self,color, dano, velocidad, veneno):
        arma = {
            color:{
                "Fuerza": dano,
                "Velocidad": velocidad,
                "Veneno": veneno
            }
        }
        return dict(arma)
