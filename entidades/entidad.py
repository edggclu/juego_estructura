import os
from abc import abstractmethod
import pygame

class entidad():
    @abstractmethod
    def __init__(self, x, y, interfaz, nombre):

        self.interfaz = interfaz
        self.forma = pygame.rect.Rect(x, y, 50, 50)
        self.forma.center = (x,y)
        self.velocidad = 0
        self.attack = False
        self.contador_sprite = 0
        self.offset = 8
        self.steps = 0
        self.lista_actual_de_sprites = []
        self.image = pygame.image.load(f'assets/Sprites/{nombre}/Idle/{os.listdir(f'assets/Sprites/{nombre}/Idle')[0]}')
        self.flip = False

    def dibujar(self):
        flip_image = pygame.transform.flip(self.image, self.flip, False)
        self.interfaz.blit(flip_image, self.forma)

    @abstractmethod
    def mover(self):
        pass

    def animar(self):
        if self.contador_sprite == self.offset:
            self.steps += 1
            if self.steps >= len(self.lista_actual_de_sprites)-1:
                self.steps = 0
                if self.attack: self.offset = 8; self.attack = False
            self.image = self.lista_actual_de_sprites[self.steps]
            self.contador_sprite = 0
        self.contador_sprite += 1

    def cargar_sprites(self, path):
        dir = f'assets/Sprites/' + path
        list = os.listdir(dir)
        scaleSize = 100
        if path.split('/')[1] == 'Idle': scaleSize = 100
        for i in range(len(list)):
            im = (pygame.image.load(dir + "/" +list[i]))
            list[i] =(pygame.transform.scale(im, (scaleSize, scaleSize)))
        return list

    def update(self):
        self.dibujar()
        self.animar()
        self.mover()
