import pygame
from entidades.entidad import entidad

class jugador(entidad):
    def __init__(self, x, y, interfaz, nombre):
        super().__init__(x, y, interfaz, nombre)
        self.velocidad = 3

        self.mover_arriba = False
        self.mover_abajo = False
        self.mover_derecha = False
        self.mover_izquierda = False
        self.attack_action = False
        self.idle = True
        self.flip = False

        self.vida = 6
        self.vida_list = self.cargar_sprites('HealthBar')
        self.vida_rect = pygame.rect.Rect(self.forma.x, self.forma.y + 100, 50,10)

        self.hitbox_attack = pygame.rect.Rect((self.hitbox.centerx + (self.hitbox.width/2 * 1.6)),self.hitbox.y +40,40,self.hitbox.height + 10)
        self.attack = False


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


        if not self.attack_action:
            if delta_x > 0: self.lista_actual_de_sprites = self.run_list; self.flip = False
            if delta_x < 0: self.lista_actual_de_sprites = self.run_list; self.flip = True
            if delta_y != 0: self.lista_actual_de_sprites = self.run_list;
            if delta_x == 0 == delta_y: self.lista_actual_de_sprites = self.idle_list
            self.attack = False
        else:
            self.lista_actual_de_sprites = self.attack_list
            #if 1 < self.steps < len(self.lista_actual_de_sprites) - 1:
            #    self.attack = True
            if self.steps == 2 and self.contador_sprite == 1:
                self.attack = True
            else:
                self.attack = False



        self.forma.x += delta_x
        self.forma.y += delta_y

        self.dibujar_vida()

        #print(delta_x, delta_y)

    def dibujar_vida(self):
        flip_image = pygame.transform.flip(self.vida_list[self.vida], False, False)
        flip_image.set_alpha(100)
        x =  1 if self.flip else -0.1
        self.interfaz.blit(flip_image, ((self.hitbox.left + (self.hitbox.width/2 * x)) - 10, self.hitbox.y + self.hitbox.height))

        a = -2.5 if self.flip else 1
        self.hitbox_attack.x = self.hitbox.centerx + (self.hitbox.width/2 * a)
        self.hitbox_attack.y = self.hitbox.y

        pygame.draw.rect(self.interfaz, (255,0,0),self.hitbox_attack)

    def key_down(self, event):
        if event.key == pygame.K_w: self.mover_arriba = True
        if event.key == pygame.K_a: self.mover_izquierda = True
        if event.key == pygame.K_d: self.mover_derecha = True
        if event.key == pygame.K_s: self.mover_abajo = True
        if event.key == pygame.K_n: self.vida -= 1
        if not self.attack_action:
            if event.key == pygame.K_j: self.attack_action = True;  self.steps = 0; self.offset = 5; self.contador_sprite = 0


    def key_up(self, event):
        if event.key == pygame.K_w: self.mover_arriba = False
        if event.key == pygame.K_a: self.mover_izquierda = False
        if event.key == pygame.K_d: self.mover_derecha = False
        if event.key == pygame.K_s: self.mover_abajo = False

