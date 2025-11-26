import pygame

# Clase boton para el menu
class boton:
    def __init__(self, texto, ventana , orden):
        # Inicializacion de atributos y recursos graficos
        self.texto = texto
        self.texto_surface = texto
        self.ventana = ventana
        self.orden = orden
        self.imagen = pygame.image.load("assets/Menu/Boton.png")
        self.alto = 85
        self.ancho = 345
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))
        self.boton_rect = self.imagen.get_rect()
        self.texto_rect = None
        self.setup()
        self.fuente = None
        self.clicked = False


    # Configuracion de posicion y renderizado de texto
    def setup(self):
        boton = pygame.image.load("assets/Menu/Boton.png")
        boton = pygame.transform.scale(boton, (self.ancho, self.alto))

        self.boton_rect = pygame.Rect(0, 0, boton.get_width(), boton.get_height())
        self.boton_rect.x = self.ventana.get_width() / 2 - boton.get_width() / 2
        self.boton_rect.y = 120 + ((self.boton_rect.height + 20)*self.orden)

        self.fuente = pygame.font.SysFont("minecraft", 30)
        self.texto_surface = self.fuente.render(self.texto, True, (255, 255, 255))
        self.texto_rect = self.texto_surface.get_rect()
        self.texto_rect.x = (self.boton_rect.x + self.boton_rect.width / 2) - self.texto_surface.get_width() / 2
        self.texto_rect.y = (self.boton_rect.y + self.boton_rect.height / 2) - self.texto_surface.get_height() / 2
        self.imagen = boton

    # Logica de interaccion con el mouse
    def update(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]
        if self.boton_rect.collidepoint(mouse):
            if click:
                self.clicked = True
            else:
                self.clicked = False
            self.animar(True)
        else:
            self.animar(False)


    # Efecto visual de escalado (Hover)
    def animar(self, bln):
        if bln:
            boton = pygame.image.load("assets/Menu/Boton.png")
            boton = pygame.transform.scale(boton, (self.ancho + 16, self.alto + 16))

            self.boton_rect = pygame.Rect(0, 0, boton.get_width(), boton.get_height())
            self.boton_rect.x = self.ventana.get_width() / 2 - self.boton_rect.width / 2
            self.boton_rect.y = 120 + ((boton.get_height()) * self.orden)

            self.texto_rect = self.texto_surface.get_rect()
            self.texto_rect.x = (self.boton_rect.x + self.boton_rect.width / 2) - self.texto_surface.get_width() / 2
            self.texto_rect.y = (self.boton_rect.y + self.boton_rect.height / 2) - self.texto_surface.get_height() / 2
            self.imagen = boton
        else:
            boton = pygame.image.load("assets/Menu/Boton.png")
            boton = pygame.transform.scale(boton, (self.ancho, self.alto))

            self.boton_rect = pygame.Rect(0, 0, boton.get_width(), boton.get_height())
            self.boton_rect.x = self.ventana.get_width() / 2 - boton.get_width() / 2
            self.boton_rect.y = 120 + ((self.boton_rect.height + 20) * self.orden)

            self.texto_rect = self.texto_surface.get_rect()
            self.texto_rect.x = (self.boton_rect.x + self.boton_rect.width / 2) - self.texto_surface.get_width() / 2
            self.texto_rect.y = (self.boton_rect.y + self.boton_rect.height / 2) - self.texto_surface.get_height() / 2
            self.imagen = boton