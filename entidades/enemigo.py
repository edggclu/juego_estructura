import pygame

from entidades.entidad import entidad
from entidades.jugador import jugador


class enemigo(entidad):
    def __init__(self, x, y, interfaz, nombre, jugador):
        super().__init__(x, y, interfaz, nombre)
        self.jugador = jugador
        self.velocidad = 2
        self.lista_actual_de_sprites = self.run_list

        self.vida = 2
        self.vof = self.hitbox.width / self.vida


    def mover(self):
        posicion_enemigo = pygame.math.Vector2(self.forma.center)
        posicion_jugador = pygame.math.Vector2(self.jugador.forma.center)

        direccion = posicion_jugador - posicion_enemigo

        if direccion[0] > 0: self.flip = False
        else: self.flip = True

        if not self.attack_action:
            #print(direccion[0])
            #print(self.forma.x)
            if abs(direccion[0]) < 30 and abs(direccion[1]) < 33:
                self.attack_action = True
                self.steps = 0; self.offset = 5; self.contador_sprite = 0
                self.lista_actual_de_sprites = self.attack_list
            else:
                self.lista_actual_de_sprites = self.run_list

        if direccion.length() > 0:
            direccion.normalize_ip()


        if self.hitbox_attack.colliderect(self.jugador.hitbox) and self.attack and not self.jugador.dano:
            self.jugador.dano = True
            self.jugador.forma.x += direccion[0] * 60
            self.jugador.forma.y += direccion[1] * 20
            self.jugador.vida -= 1

        # Recibe daño
        if self.hitbox.colliderect(self.jugador.hitbox_attack) and self.jugador.attack:
            self.vida -= 1
            self.forma.x += direccion[0]*-50
            self.dano = True
            print('Daño')

        if direccion.length() > 0:
            direccion.normalize_ip()
        if not self.attack_action:
            self.forma.move_ip(direccion * self.velocidad)

        #pygame.draw.rect(self.interfaz, (255,0,0),self.hitbox)

