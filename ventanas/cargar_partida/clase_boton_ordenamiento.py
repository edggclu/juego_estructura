import pygame


class BotonOrdenamiento:
    #Representa un botón para seleccionar un criterio de ordenamiento de las partidas guardadas (Tiempo, Dinero, Kills)

    def __init__(self, ventana, x, y, texto, ruta_icono):
        # Inicializa el botón de ordenamiento.

        #Parametros:
        # ventana: La superficie principal de Pygame
        # x: Posición X del botón
        # y: Posición Y del botón
        # texto: El texto a mostrar en el botón
        # ruta_icono: La ruta al archivo de imagen del icono a mostrar

        self.ventana = ventana
        self.hovered = False # Estado para saber si el mouse está encima

        # Cargar y escalar la imagen base del botón
        self.image = pygame.image.load("assets/Menu/Boton.png")
        self.image = pygame.transform.scale(self.image, (130, 45))  # Tamaño ajustado
        self.rect = self.image.get_rect(topleft=(x, y))                  # Rect para detección de colisiones

        # Cargar y escalar el icono
        self.icono = pygame.image.load(ruta_icono)
        self.icono = pygame.transform.scale(self.icono, (25, 25))
        self.icono_rect = self.icono.get_rect()
        # Posicionamos el icono a la izquierda dentro del botón
        self.icono_rect.left = self.rect.left + 10
        self.icono_rect.centery = self.rect.centery

        # Configurar el texto
        pygame.font.init()
        self.font = pygame.font.SysFont('minecraft', 22)
        self.texto_surf = self.font.render(texto, True, (255, 255, 255))
        self.texto_rect = self.texto_surf.get_rect()
        # Posicionamos el texto a la derecha del icono
        self.texto_rect.left = self.icono_rect.right + 8
        self.texto_rect.centery = self.rect.centery

    def update(self):
        #Actualiza el estado del botón (detecta el evento de hover).

        pos_mouse = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos_mouse):
            self.hovered = True
        else:
            self.hovered = False

    def draw(self):
        #Dibuja el botón (fondo, icono y texto) en la ventana

        # Dibujar fondo, icono y texto
        self.ventana.blit(self.image, self.rect)
        self.ventana.blit(self.icono, self.icono_rect)
        self.ventana.blit(self.texto_surf, self.texto_rect)

        # Efecto de borde blanco si el mouse está encima
        if self.hovered:
            pygame.draw.rect(self.ventana, (255, 255, 255), self.rect, 2, border_radius=10)