import pygame

from entidades.jugador import jugador


class enemigo:
    def __init__(self, x,y, image):
        self.image = image
        self.forma = pygame.rect.Rect(x,y,10,10)
        self.forma.center = (x,y)
        self.velocidad = 2

    def dibujar(self, interfaz):
        interfaz.blit(self.image, self.forma)

    def seguir_jugador(self, jugador):
        posicion_enemigo = pygame.math.Vector2(self.forma.center)
        posicion_jugador = pygame.math.Vector2(jugador.forma.center)

        direccion = posicion_jugador - posicion_enemigo

        if direccion.length() > 0:
            direccion.normalize_ip()

        self.forma.move_ip(direccion * self.velocidad)


