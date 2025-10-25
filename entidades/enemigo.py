import pygame

from entidades.entidad import entidad
from entidades.jugador import jugador


class enemigo(entidad):
    def __init__(self, x, y, interfaz, nombre, jugador):
        super().__init__(x, y, interfaz, nombre)
        self.jugador = jugador
        self.velocidad = 2
        self.lista_actual_de_sprites = self.run_list

        self.vida = 1


    def mover(self):
        posicion_enemigo = pygame.math.Vector2(self.forma.center)
        posicion_jugador = pygame.math.Vector2(self.jugador.forma.center)

        direccion = posicion_jugador - posicion_enemigo

        if direccion[0] > 0: self.flip = False
        else: self.flip = True

        if not self.attack_action:
            #print(direccion[1])
            if abs(direccion[0]) < 20 and abs(direccion[1]) < 33:
                self.attack = True
                self.steps = 0; self.offset = 5; self.contador_sprite = 0
                self.lista_actual_de_sprites = self.attack_list
            else:
                self.lista_actual_de_sprites = self.run_list

        if direccion.length() > 0:
            direccion.normalize_ip()

        #self.forma.move_ip(direccion * self.velocidad)


        # Recibe daño
        if self.hitbox.colliderect(self.jugador.hitbox_attack) and self.jugador.attack:
            self.vida -= 1
            print('Daño')

        #pygame.draw.rect(self.interfaz, (255,0,0),self.hitbox)

