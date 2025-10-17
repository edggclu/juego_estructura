import pygame
from entidades.entidad import entidad

class jugador(entidad):
    def __init__(self, x, y, interfaz, image_path):
        super().__init__(x, y, interfaz, image_path)
        self.mover_arriba = False
        self.mover_abajo = False
        self.mover_derecha = False
        self.mover_izquierda = False
        self.lista_sprites = []
        self.cargar_sprites(self.lista_sprites,"assets/player")

    def mover(self):
        delta_x = 0
        delta_y = 0
        if self.mover_derecha:
            delta_x = 5
        if self.mover_izquierda:
            delta_x = -5
        if self.mover_arriba:
            delta_y = -5
        if self.mover_abajo:
            delta_y = 5

        self.forma.x += delta_x
        self.forma.y += delta_y

    def key_down(self, event):
        if event.key == pygame.K_w: self.mover_arriba = True
        if event.key == pygame.K_a: self.mover_izquierda = True
        if event.key == pygame.K_d: self.mover_derecha = True
        if event.key == pygame.K_s: self.mover_abajo = True

    def key_up(self, event):
        if event.key == pygame.K_w: self.mover_arriba = False
        if event.key == pygame.K_a: self.mover_izquierda = False
        if event.key == pygame.K_d: self.mover_derecha = False
        if event.key == pygame.K_s: self.mover_abajo = False

