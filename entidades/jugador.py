import pygame
from entidades.entidad import entidad

class jugador(entidad):
    def __init__(self, x, y, interfaz, image_path):
        super().__init__(x, y, interfaz, image_path)
        self.mover_arriba = False
        self.mover_abajo = False
        self.mover_derecha = False
        self.mover_izquierda = False
        self.idle = True
        self.velocidad = 3

        #listas de sprites
        self.walking = self.cargar_sprites('assets/skeleton/walking')
        self.idle = self.cargar_sprites("assets/skeleton/idle")

        self.lista_actual_de_sprites = self.idle

    def mover(self):
        delta_x = 0
        delta_y = 0
        if self.mover_derecha:
            delta_x = self.velocidad
        if self.mover_izquierda:
            delta_x = -self.velocidad
        if self.mover_arriba:
            delta_y = -self.velocidad
        if self.mover_abajo:
            delta_y = self.velocidad

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

