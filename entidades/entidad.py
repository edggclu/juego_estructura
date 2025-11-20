import os
from abc import abstractmethod, ABC

import pygame

class entidad(ABC):
    @abstractmethod
    def __init__(self, x, y, interfaz, nombre, arma):
        self.arma = arma
        self.color = nombre.split('_')[1]
        self.velocidad = self.arma[self.color]["Velocidad"]
        self.fuerza = self.arma[self.color]["Fuerza"]
        self.curacion = self.arma[self.color]["Curacion"]

        self.vivo = True

        #self.velocidad = 3

        self.interfaz = interfaz
        self.contador_sprite = 0
        self.offset = 24//self.velocidad
        self.steps = 0

        self.nombre = nombre
        self.run_list = self.cargar_sprites(f'{self.nombre}/Run')
        self.idle_list = self.cargar_sprites(f'{self.nombre}/Idle')
        self.attack_list = self.cargar_sprites(f'{self.nombre}/Attack')
        self.death_list = self.cargar_sprites(f'{self.nombre}/Death')
        self.lista_actual_de_sprites = self.idle_list
        self.image = self.lista_actual_de_sprites[0]
        #self.image = pygame.image.load(f'assets/Sprites/{nombre}/Idle/{os.listdir(f'assets/Sprites/{nombre}/Idle')[0]}')

        self.attack_action = False
        self.flip = False
        self.alpha = 255

        self.forma = pygame.rect.Rect((self.image.get_rect()))
        self.forma.center = (x,y)

        self.hitbox = pygame.rect.Rect(self.forma.centerx - 25, self.forma.bottom -50, 50,65)
        self.hitbox_attack = pygame.rect.Rect((self.hitbox.centerx + (self.hitbox.width / 2 * 1.6)), self.hitbox.y + 40,
                                              30, self.hitbox.height + 10)
        self.vida = 15
        self.max_vida = self.vida
        self.vof = self.hitbox.width / self.vida
        self.vida_rect = pygame.rect.Rect(self.hitbox.left,self.hitbox.bottom +5,self.hitbox.width,8)
        self.color_vida = (255,0,0)

        self.attack = False
        self.dano = False
        self.dano_counter = 0
        self.reps = 0

    def dibujar(self):
        flip_image = pygame.transform.flip(self.image, self.flip, False)
        flip_image.set_alpha(self.alpha)
        self.hitbox.x = self.forma.centerx - 25
        self.hitbox.y = self.forma.bottom - 70
        self.interfaz.blit(flip_image, self.forma)

    @abstractmethod
    def mover(self):
        pass

    def animar(self):
        if self.contador_sprite == self.offset:
            self.steps += 1
            if self.steps >= len(self.lista_actual_de_sprites)-1:
                self.steps = 0
                if self.attack_action: self.offset = 24//self.velocidad; self.attack_action = False
                if self.lista_actual_de_sprites == self.death_list:
                    self.vivo = False
            self.image = self.lista_actual_de_sprites[self.steps]
            self.contador_sprite = 0
        self.contador_sprite += 1

        if self.attack_action:
            if self.steps == 3 and self.contador_sprite == 1:
                self.attack = True
            else:
                self.attack = False


    def cargar_sprites(self, path):
        dir = f'assets/Sprites/' + path
        list = os.listdir(dir)
        scaleSize = 3
        #if path == 'HealthBar': scaleSize = 1
        for i in range(len(list)):
            im = (pygame.image.load(dir + "/" +list[i]).convert_alpha())
            list[i] =(pygame.transform.scale(im, (im.get_width() * scaleSize, im.get_height()* scaleSize)))
        return list

    def dibujar_vida(self):
        self.vida_rect.left, self.vida_rect.top = self.hitbox.left,self.hitbox.bottom +5
        if self.vida < self.max_vida:
            pygame.draw.rect(self.interfaz,self.color_vida,self.vida_rect,1)
            pygame.draw.rect(self.interfaz,self.color_vida,(self.vida_rect.left,self.vida_rect.top,self.vof * self.vida,self.vida_rect.height))

        a = -2.5 if self.flip else 1
        self.hitbox_attack.x = self.hitbox.centerx + (self.hitbox.width/2 * a)
        self.hitbox_attack.y = self.hitbox.y

        #pygame.draw.rect(self.interfaz, (255,0,0),self.hitbox, 1)
        #pygame.draw.rect(self.interfaz,(0,255,0),self.hitbox_attack, 1)
        if self.dano:
            if self.dano_counter == 4:
                self.alpha = 50
            elif self.dano_counter == 8:
                self.alpha = 255
                self.reps += 1
                self.dano_counter = 0
            if self.reps == 3:
                self.alpha = 255
                self.dano = False
                self.dano_counter = 0
                self.reps = 0

            self.dano_counter += 1

    def update(self):
        self.dibujar_vida()
        self.dibujar()
        self.animar()
        self.mover()
