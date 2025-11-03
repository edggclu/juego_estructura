import os
import random

import pygame


class boton_eleccion_np():
    def __init__(self,ventana, x, y , ancho, alto, clase_personaje,color_personaje):
        self.ventana = ventana
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto

        self.clase_personaje = clase_personaje
        self.color_personaje = color_personaje

        self.lista_sprites_idle = self.setup("Idle")
        self.lista_sprites_attack = self.setup("Attack")
        self.lista_actual_sprites = self.lista_sprites_idle
        im = self.lista_actual_sprites[0]

        self.fondo = pygame.image.load('ventanas/menu/BaseMenu.png')
        self.fondo = pygame.transform.scale(self.fondo,(self.ancho,self.alto))
        self.fondo_rect = pygame.rect.Rect(self.x, self.y, self.ancho, self.alto)
        self.image = im
        self.image_rect = pygame.rect.Rect(self.x + (self.ancho/10)/3, self.y - self.ancho/10, self.ancho, self.alto)

        self.contador_sprite = 0
        self.offset = 5
        self.steps = random.randint(0, len(self.lista_actual_sprites)-1)

        self.contador_crecer = 0

        self.animar_bool = True
        self.crecer_bool = False
        self.hover = False
        self.clicked = False

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()[0]
        if self.fondo_rect.collidepoint(mouse_pos):
            self.hover = True
            if mouse_click == 1:
                self.clicked = True
            else:
                self.clicked = False
        else:
            self.lista_actual_sprites = self.lista_sprites_idle
            #self.steps = 0
            self.hover = False


        if self.animar_bool:
            self.animar()
        else:
            self.steps = 0
            self.lista_actual_sprites = self.lista_sprites_idle
            self.image = self.lista_actual_sprites[self.steps]

        self.crecer()
        self.ventana.blit(self.fondo, self.fondo_rect)
        self.ventana.blit(self.image, self.image_rect)

    def animar(self):
        if self.contador_sprite == self.offset:
            self.steps += 1
            if self.steps >= len(self.lista_actual_sprites) - 1:
                self.steps = 0
            self.image = self.lista_actual_sprites[self.steps]
            self.contador_sprite = 0
        self.contador_sprite += 1

    def crecer(self):
        self.fondo_rect.width = self.ancho + 24
        self.fondo_rect.height = self.alto + 24
        self.fondo_rect.x = self.x - 24
        self.fondo_rect.y = self.y - 24
        self.fondo = pygame.image.load('ventanas/menu/BaseMenu.png')
        self.fondo = pygame.transform.scale(self.fondo,(self.fondo_rect.width,self.fondo_rect.width))

    def setup(self, Action='Idle'):
        dir = f'assets/Sprites/{self.clase_personaje}_{self.color_personaje}/{Action}'
        list = os.listdir(dir)
        for i in range(len(list)):
            im = (pygame.image.load(dir + "/" + list[i]).convert_alpha())
            list[i] = (pygame.transform.scale(im, (self.ancho, self.alto)))
        return list
