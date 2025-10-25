import os
from abc import abstractmethod
import pygame

class entidad():
    @abstractmethod
    def __init__(self, x, y, interfaz, nombre):

        self.interfaz = interfaz
        self.velocidad = 0
        self.vida = 0
        self.attack_action = False
        self.contador_sprite = 0
        self.offset = 8
        self.steps = 0
        self.nombre = nombre
        self.run_list = self.cargar_sprites(f'{self.nombre}/Run')
        self.idle_list = self.cargar_sprites(f'{self.nombre}/Idle')
        self.attack_list = self.cargar_sprites(f'{self.nombre}/Attack')
        self.lista_actual_de_sprites = self.idle_list
        self.image = self.lista_actual_de_sprites[0]
        #self.image = pygame.image.load(f'assets/Sprites/{nombre}/Idle/{os.listdir(f'assets/Sprites/{nombre}/Idle')[0]}')
        self.flip = False

        self.forma = pygame.rect.Rect((self.image.get_rect()))
        self.forma.center = (x,y)

        self.hitbox = pygame.rect.Rect(self.forma.centerx - 25, self.forma.bottom -50, 50,65)


    def dibujar(self):
        flip_image = pygame.transform.flip(self.image, self.flip, False)
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
                if self.attack_action: self.offset = 8; self.attack_action = False
            self.image = self.lista_actual_de_sprites[self.steps]
            self.contador_sprite = 0
        self.contador_sprite += 1

    def cargar_sprites(self, path):
        dir = f'assets/Sprites/' + path
        list = os.listdir(dir)
        scaleSize = 3
        if path == 'HealthBar': scaleSize = 1
        for i in range(len(list)):
            im = (pygame.image.load(dir + "/" +list[i]).convert_alpha())
            list[i] =(pygame.transform.scale(im, (im.get_width() * scaleSize, im.get_height()* scaleSize)))
        return list

    def update(self):
        self.dibujar()
        self.animar()
        self.mover()
