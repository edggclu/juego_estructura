import pygame
class jugador:
    def __init__(self, x,y, image):
        self.image = image
        self.forma = pygame.Rect(0,0,50,50)
        self.forma.center = (x,y)


    def mover(self,delta_x,delta_y):
        self.forma.x = self.forma.x + delta_x
        self.forma.y = self.forma.y + delta_y

    def dibujar(self, interfaz):
        #pygame.draw.rect(interfaz,(255,255,0),self.forma)
        interfaz.blit(self.image, self.forma)


