import pygame

from entidades.enemigo import enemigo
from entidades.jugador import jugador
from mapa import Map
import random


class ventana_juego:
    def __init__(self, ventana, partida):
        self.ventana = ventana
        self.partida = partida



        # Instancia del jugador
        self.jugador = jugador(ventana.get_width() / 2,
                               ventana.get_height() / 2,
                               ventana,
                               f'{self.partida.tipo_personaje}',
                               self.partida.arma)

        # Instancia del enemigo
        self.enemigo = enemigo(200, 100, ventana, f'vampire_{self.jugador.color}', self.jugador, self.partida.arma)
        #self.enemigo.vida = 10

        self.entidades = [self.jugador, self.enemigo]

        for i in range(20):
            self.entidades.append(enemigo(random.randint(100, 200), random.randint(100, 200),ventana,
                                          f'vampire_{self.jugador.color}',
                                          self.jugador, self.partida.arma))
        self.mapa_juego = Map("assets/mapa/mapa2.tmx")

        self.fondo_mapa = self.mapa_juego.crear_mapa()

    def update(self):
        self.ventana.fill((0, 0, 0))
        x = self.jugador.relative_x
        y = self.jugador.relative_y
        self.ventana.blit(self.fondo_mapa, (x, y))
        pygame.display.set_caption(f'{self.jugador.hitbox.x // 16, self.jugador.hitbox.y // 16}')
        self.jugador.gid_lados = self.mapa_juego.get_piso(self.jugador)
        self.jugador.camara[0] = (-y + self.jugador.hitbox.top)
        self.jugador.camara[2] = (self.mapa_juego.alto_mapa + y - self.jugador.hitbox.bottom - self.jugador.hitbox.height / 2)
        self.jugador.camara[1] = (self.mapa_juego.ancho_mapa + x - self.jugador.hitbox.right - self.jugador.hitbox.width / 2)
        self.jugador.camara[3] = (-x + self.jugador.hitbox.left)

        for entidad in self.entidades:
            if entidad.vivo:
                entidad.update()

        #pygame.display.set_caption(f'{type(self.jugador.color)}')

