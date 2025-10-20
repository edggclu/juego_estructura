from turtledemo.clock import setup

import pygame
class boton:
    def __init__(self, texto, ventana , orden):
        self.texto = texto
        self.texto_surface = texto
        self.ventana = ventana
        self.orden = orden
        self.imagen = pygame.image.load("boton.png")
        self.boton_rect = self.imagen.get_rect()
        self.texto_rect = None
        self.setup()
        self.fuente = None


    def setup(self):
        boton = pygame.image.load("boton.png")
        boton = pygame.transform.scale(boton, (boton.get_width(), boton.get_height()))

        self.boton_rect = pygame.Rect(0, 0, boton.get_width(), boton.get_height())
        self.boton_rect.x = self.ventana.get_width() / 2 - boton.get_width() / 2
        self.boton_rect.y = 120 + ((self.boton_rect.height + 20)*self.orden)

        self.fuente = pygame.font.SysFont("comicsans", 30)
        self.texto_surface = self.fuente.render(self.texto, True, (255, 255, 255))
        self.texto_rect = self.texto_surface.get_rect()
        self.texto_rect.x = (self.boton_rect.x + self.boton_rect.width / 2) - self.texto_surface.get_width() / 2
        self.texto_rect.y = (self.boton_rect.y + self.boton_rect.height / 2) - self.texto_surface.get_height() / 2
        self.imagen = boton

    def update(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]
        if self.boton_rect.collidepoint(mouse):
            if click:
                print("boton")
            self.animar(True)
        else:
            self.animar(False)


    def animar(self, bln):
        if bln:
            boton = pygame.image.load("boton.png")
            boton = pygame.transform.scale(boton, (boton.get_width() + 15, boton.get_height() + 15))

            self.boton_rect = pygame.Rect(0, 0, boton.get_width(), boton.get_height())
            self.boton_rect.x = self.ventana.get_width() / 2 - self.boton_rect.width / 2
            self.boton_rect.y = 120 + ((boton.get_height()) * self.orden) - 7

            self.fuente = pygame.font.SysFont("comicsans", 30)
            self.texto_surface = self.fuente.render(self.texto, True, (255, 255, 255))
            self.texto_rect = self.texto_surface.get_rect()
            self.texto_rect.x = (self.boton_rect.x + self.boton_rect.width / 2) - self.texto_surface.get_width() / 2
            self.texto_rect.y = (self.boton_rect.y + self.boton_rect.height / 2) - self.texto_surface.get_height() / 2
            self.imagen = boton
        else:
            boton = pygame.image.load("boton.png")
            boton = pygame.transform.scale(boton, (boton.get_width(), boton.get_height()))

            self.boton_rect = pygame.Rect(0, 0, boton.get_width(), boton.get_height())
            self.boton_rect.x = self.ventana.get_width() / 2 - boton.get_width() / 2
            self.boton_rect.y = 120 + ((self.boton_rect.height + 20) * self.orden)

            self.fuente = pygame.font.SysFont("comicsans", 30)
            self.texto_surface = self.fuente.render(self.texto, True, (255, 255, 255))
            self.texto_rect = self.texto_surface.get_rect()
            self.texto_rect.x = (self.boton_rect.x + self.boton_rect.width / 2) - self.texto_surface.get_width() / 2
            self.texto_rect.y = (self.boton_rect.y + self.boton_rect.height / 2) - self.texto_surface.get_height() / 2
            self.imagen = boton

