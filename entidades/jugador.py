import pygame
from entidades.entidad import entidad

class jugador(entidad):
    def __init__(self, x, y, interfaz, nombre, arma):
        super().__init__(x, y, interfaz, nombre, arma)

        self.mover_arriba = False
        self.mover_abajo = False
        self.mover_derecha = False
        self.mover_izquierda = False
        self.attack_action = False

        self.piso = 0

        self.idle = True
        self.flip = False

        self.vida = 25
        self.vof = self.hitbox.width / self.vida
        self.gid_lados = (0,0,0,0)

        #self.hitbox_attack = pygame.rect.Rect((self.hitbox.centerx + (self.hitbox.width/2 * 1.6)),self.hitbox.y +40,40,self.hitbox.height + 10)
        self.attack = False
        self.color_vida = (0,255,0)

        self.delta_y = self.delta_x = 0
        self.camara = [0,0,0,0]
        self.camara_max_bottom = self.interfaz.get_height() - self.hitbox.bottom - self.hitbox.height/2
        self.camara_max_top = 0 + self.hitbox.top
        self.camara_max_left = 0 + self.hitbox.left
        self.camara_max_right = self.interfaz.get_width() - self.hitbox.right - self.hitbox.width/2
        self.relative_x = self.relative_y = 0



    def mover(self):
        self.delta_x = 0
        self.delta_y = 0



        if self.mover_derecha:
            self.delta_x = self.velocidad
        if self.mover_izquierda:
            self.delta_x = -self.velocidad
        if self.mover_arriba:
            self.delta_y = -self.velocidad
        if self.mover_abajo:
            self.delta_y = self.velocidad


        if not self.attack_action:
            if self.delta_x > 0: self.lista_actual_de_sprites = self.run_list; self.flip = False
            if self.delta_x < 0: self.lista_actual_de_sprites = self.run_list; self.flip = True
            if self.delta_y != 0: self.lista_actual_de_sprites = self.run_list;
            if self.delta_x == 0 == self.delta_y: self.lista_actual_de_sprites = self.idle_list
            self.attack = False
        else:
            self.lista_actual_de_sprites = self.attack_list
            #if 1 < self.steps < len(self.lista_actual_de_sprites) - 1:
            #    self.attack = True



        if self.gid_lados[0]!= 0 and self.delta_y == -self.velocidad:
            self.delta_y = 0
        if self.gid_lados[1]!= 0 and self.delta_x == self.velocidad:
            self.delta_x = 0
        if self.gid_lados[2] != 0 and self.delta_y == self.velocidad:
            self.delta_y = 0
        if self.gid_lados[3]!= 0 and self.delta_x == -self.velocidad:
            self.delta_x = 0

        if abs(self.camara_max_bottom) > self.camara[2]:
            self.forma.y += self.delta_y
            self.delta_y = 0
        elif abs(self.camara_max_top) > self.camara[0]:
            self.forma.y += self.delta_y
            self.delta_y = 0
        if abs(self.camara_max_right) > self.camara[1]:
            self.forma.x += self.delta_x
            self.delta_x = 0
        elif abs(self.camara_max_left) > self.camara[3] or self.hitbox.left <= self.relative_y + 20:
            self.forma.x += self.delta_x
            self.delta_x = 0

        self.relative_x += - self.delta_x
        self.relative_y += - self.delta_y


        #self.dibujar_vida()

        #print(self.delta_x, self.delta_y)

    def dibujar_vida(self):
        super().dibujar_vida()

    def key_down(self, event):
        if event.key == pygame.K_w: self.mover_arriba = True
        if event.key == pygame.K_a: self.mover_izquierda = True
        if event.key == pygame.K_d: self.mover_derecha = True
        if event.key == pygame.K_s: self.mover_abajo = True
        if event.key == pygame.K_n: self.vida -= 1
        if not self.attack_action:
            if event.key == pygame.K_j: self.attack_action = True;  self.steps = 0; self.offset = 15//self.velocidad; self.contador_sprite = 0


    def key_up(self, event):
        if event.key == pygame.K_w: self.mover_arriba = False
        if event.key == pygame.K_a: self.mover_izquierda = False
        if event.key == pygame.K_d: self.mover_derecha = False
        if event.key == pygame.K_s: self.mover_abajo = False

