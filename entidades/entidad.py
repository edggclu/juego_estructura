import os
import pygame

class entidad():
    def __init__(self, x, y, interfaz, image_path):
        self.image = pygame.image.load(image_path)
        self.interfaz = interfaz
        self.forma = pygame.rect.Rect(x, y, 50, 50)
        self.forma.center = (x,y)
        self.velocidad = 0
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.contador_sprite = 0
        self.offset = 6
        self.steps = 0
        #self.lista_sprites = []

    def dibujar(self):
        self.interfaz.blit(self.image, self.forma)

    def mover(self):
        pass

    def animar(self):
        if self.contador_sprite == self.offset:
            self.steps += 1
            if self.steps >= len(self.lista_sprites)-1:
                self.steps = 0
            self.image = self.lista_sprites[self.steps]
            self.contador_sprite = 0
        self.contador_sprite += 1

    def update(self):
        self.animar()
        self.mover()
        self.dibujar()

    def cargar_sprites(self, lista, path):
        list = os.listdir(path)
        for i in range(len(list)):
            im = (pygame.image.load(path + "/" +list[i]))
            lista.append(pygame.transform.scale(im, (100, 100)))
        return lista
