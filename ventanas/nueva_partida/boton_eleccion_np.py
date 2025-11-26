import os
import random

import pygame


# Clase para el boton de seleccion de personaje en nueva partida
class boton_eleccion_np():
    def __init__(self, ventana, x, y, ancho, alto, clase_personaje, color_personaje):
        # Inicializacion de variables y dimensiones
        self.ventana = ventana
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto

        self.clase_personaje = clase_personaje
        self.color_personaje = color_personaje

        # Configuracion y carga de listas de sprites
        self.lista_sprites_idle = self.setup("Idle")
        self.lista_sprites_attack = self.setup("Attack")
        self.lista_sprites_run = self.setup("Run")
        self.arreglo_de_sprites = [self.lista_sprites_idle,
                                   self.lista_sprites_run]
        self.lista_actual_sprites = self.lista_sprites_idle
        im = self.lista_actual_sprites[0]

        # Configuracion de imagen de fondo y rectangulos de colision
        self.fondo = pygame.image.load('assets/Menu/BaseMenu.png')
        self.fondo = pygame.transform.scale(self.fondo, (self.ancho, self.alto))
        self.fondo_rect = pygame.rect.Rect(self.x, self.y, self.ancho, self.alto)
        self.image = im
        self.image_rect = pygame.rect.Rect(self.x + (self.ancho / 10) / 3, self.y - self.ancho / 10, self.ancho,
                                           self.alto)

        # Variables de control de animacion
        self.contador_sprite = 0
        self.offset = 5
        self.steps = random.randint(0, len(self.lista_actual_sprites) - 1)

        self.contador_crecer = 0

        # Estados booleanos del boton
        self.animar_bool = True
        self.animar_random = False
        self.Flip = False
        self.crecer_bool = False
        self.hover = False
        self.clicked = False

    def update(self):
        # Obtencion de posicion y estado del mouse
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()[0]

        # Logica de colision y clic
        if self.fondo_rect.collidepoint(mouse_pos):
            self.hover = True
            if mouse_click == 1:
                self.clicked = True
                pygame.mouse.set_pos(self.ventana.get_width() / 2, self.ventana.get_height() / 2)
            else:
                self.clicked = False
            # self.animar_bool = False
        else:
            # self.animar_random = True
            # self.lista_actual_sprites = self.lista_sprites_idle
            self.hover = False

        # Actualizacion de animacion
        if self.animar_bool:
            self.animar()
        else:
            self.steps = 0
            self.Flip = False
            self.lista_actual_sprites = self.lista_sprites_idle
            self.image = self.lista_actual_sprites[self.steps]

        # Logica de escalado
        self.crecer()

        # Renderizado final con posible inversion de imagen
        flip_image = pygame.transform.flip(self.image, self.Flip, False)
        self.ventana.blit(self.fondo, self.fondo_rect)
        self.ventana.blit(flip_image, self.image_rect)

    def animar(self):
        # Control de frames y bucle de animacion
        # flip
        if self.contador_sprite == self.offset:
            self.steps += 1
            if self.steps >= len(self.lista_actual_sprites) - 1:
                self.steps = 0
                if self.animar_random:
                    self.lista_actual_sprites = self.arreglo_de_sprites[random.randint(0, 1)]
                    self.Flip = True if random.randint(0, 1) == 1 else False
            self.image = self.lista_actual_sprites[self.steps]
            self.contador_sprite = 0
        self.contador_sprite += 1

    def crecer(self):
        # Calculo de aumento o disminucion de tamaño al hacer hover
        if self.hover:
            if self.contador_crecer < 24:
                self.crecer_bool = True
                self.contador_crecer += 8
            else:
                self.crecer_bool = False
        else:
            if self.contador_crecer > 0:
                self.crecer_bool = True
                self.contador_crecer -= 8
            else:
                self.crecer_bool = False

        # Aplicacion de nuevas dimensiones al fondo
        if self.crecer_bool:
            self.fondo_rect.width = self.ancho + self.contador_crecer
            self.fondo_rect.height = self.alto + self.contador_crecer
            self.fondo_rect.x = self.x - self.contador_crecer / 2
            self.fondo_rect.y = self.y - self.contador_crecer / 2
            self.fondo = pygame.image.load('assets/Menu/BaseMenu.png')
            self.fondo = pygame.transform.scale(self.fondo, (self.fondo_rect.width, self.fondo_rect.width))

    def setup(self, Action='Idle'):
        # Carga masiva de imagenes desde directorio
        dir = f'assets/Sprites/{self.clase_personaje}_{self.color_personaje}/{Action}'
        list = os.listdir(dir)
        for i in range(len(list)):
            im = (pygame.image.load(dir + "/" + list[i]).convert_alpha())
            list[i] = (pygame.transform.scale(im, (self.ancho, self.alto)))
        return list