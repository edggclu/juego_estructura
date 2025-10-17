import pygame
class entidad():
    def __init__(self, x, y, interfaz, image_path):
        self.image = pygame.image.load(image_path)
        self.interfaz = interfaz
        self.forma = pygame.rect.Rect(x, y, 50, 50)
        self.forma.center = (x,y)
        self.velocidad = 0
        self.image = pygame.transform.scale(self.image, (100, 100))


    def dibujar(self):
        self.interfaz.blit(self.image, self.forma)

    def mover(self):
        pass

    def update(self):
        self.mover()
        self.dibujar()
