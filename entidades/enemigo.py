import pygame

from entidades.entidad import entidad
from entidades.jugador import jugador


class enemigo(entidad):
    def __init__(self, x, y, interfaz, nombre, jugador, arma):
        super().__init__(x, y, interfaz, nombre, arma)
        self.jugador = jugador
        self.lista_actual_de_sprites = self.run_list

        self.delta_x = 0
        self.delta_y = 0

    def mover(self):
        posicion_enemigo = pygame.math.Vector2(self.forma.center)
        posicion_jugador = pygame.math.Vector2(self.jugador.forma.center)

        direccion = posicion_jugador - posicion_enemigo

        if direccion[0] > 0: self.flip = False
        else: self.flip = True

        if not self.attack_action:
            if abs(direccion[0]) < 30 and abs(direccion[1]) < 33:
                self.attack_action = True
                self.steps = 0; self.offset = 5; self.contador_sprite = 0
                self.lista_actual_de_sprites = self.attack_list
            else:
                if self.lista_actual_de_sprites != self.death_list:
                    self.lista_actual_de_sprites = self.run_list

        if direccion.length() > 0:
            direccion.normalize_ip()


        if self.hitbox_attack.colliderect(self.jugador.hitbox) and self.attack and not self.jugador.dano:
            golpe_x = direccion[0] * 60
            golpe_y = direccion[1] * 20
            self.jugador.dano = True
            self.jugador.forma.x += golpe_x
            self.jugador.forma.y += golpe_y
            self.jugador.vida -= 1
            self.jugador.update_camara()

        # Recibe daño
        if self.hitbox.colliderect(self.jugador.hitbox_attack) and self.jugador.attack:
            self.vida -= self.jugador.fuerza
            self.forma.x += direccion[0]*-50
            self.dano = True
            #print('Daño')

        if direccion.length() > 0:
            direccion.normalize_ip()
        if not self.attack_action:
            if self.delta_x > self.jugador.relative_x:
                movimiento_x = -self.jugador.velocidad
                self.delta_x = self.jugador.relative_x
            elif self.delta_x < self.jugador.relative_x:
                movimiento_x = self.jugador.velocidad
                self.delta_x = self.jugador.relative_x
            else:
                movimiento_x = 0
            if self.delta_y > self.jugador.relative_y:
                movimiento_y = -self.jugador.velocidad
                self.delta_y = self.jugador.relative_y
            elif self.delta_y < self.jugador.relative_y:
                movimiento_y = self.jugador.velocidad
                self.delta_y = self.jugador.relative_y
            else:
                movimiento_y = 0
            if self.vida > 0:
                self.forma.move_ip(direccion * self.velocidad + (movimiento_x, movimiento_y))

            else:
                self.forma.move_ip(direccion + (movimiento_x, movimiento_y))


        if self.vida <= 0:
            if self.lista_actual_de_sprites is not self.death_list:
                #self.velocidad = 0
                self.contador_sprite = 0
                self.lista_actual_de_sprites = self.death_list
                self.offset = 4

        #pygame.display.set_caption(f'{self.contador_sprite}')
        #pygame.draw.rect(self.interfaz, (255,0,0),self.hitbox)

