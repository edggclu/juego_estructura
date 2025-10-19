import pygame
from entidades.entidad import entidad

class jugador(entidad):
    def __init__(self, x, y, interfaz, nombre):
        super().__init__(x, y, interfaz, nombre)
        self.velocidad = 3
        self.nombre = nombre
        self.run_list = self.cargar_sprites(f'{self.nombre}/Run')
        self.idle_list = self.cargar_sprites(f'{self.nombre}/Idle')
        self.attack_list = self.cargar_sprites(f'{self.nombre}/Attack')
        self.mover_arriba = False
        self.mover_abajo = False
        self.mover_derecha = False
        self.mover_izquierda = False
        self.attack = False
        self.idle = True
        self.flip = False

        self.lista_actual_de_sprites = self.idle_list
        self.image = self.lista_actual_de_sprites[0]


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


        if not self.attack:
            if delta_x > 0: self.lista_actual_de_sprites = self.run_list; self.flip = False
            if delta_x < 0: self.lista_actual_de_sprites = self.run_list; self.flip = True
            if delta_y != 0: self.lista_actual_de_sprites = self.run_list;
            if delta_x == 0 == delta_y: self.lista_actual_de_sprites = self.idle_list
        else: self.lista_actual_de_sprites = self.attack_list

        self.forma.x += delta_x
        self.forma.y += delta_y

        #print(delta_x, delta_y)

    def key_down(self, event):
        if event.key == pygame.K_w: self.mover_arriba = True
        if event.key == pygame.K_a: self.mover_izquierda = True
        if event.key == pygame.K_d: self.mover_derecha = True
        if event.key == pygame.K_s: self.mover_abajo = True
        if self.attack == False:
            if event.key == pygame.K_e: self.attack = True;  self.steps = 0; self.offset = 5; self.contador_sprite = 0


    def key_up(self, event):
        if event.key == pygame.K_w: self.mover_arriba = False
        if event.key == pygame.K_a: self.mover_izquierda = False
        if event.key == pygame.K_d: self.mover_derecha = False
        if event.key == pygame.K_s: self.mover_abajo = False

