
import pygame
class boton_cargar_partida:

    def __init__(self, ventana, x, y, tiempo, imagen_personaje, velocidad, enemigos_eliminados, nombre_jugador):
        pygame.font.init()  #Modulo fuente para los textos
        self.font = pygame.font.Font(None, 24)  # Fuente por defecto, tamaño 24
        self.ventana = ventana
        self.hovered = False            # Muestra el cuadro a la derecha con las estadisticas

        #TEXTOS A USAR EN EL BOTÓN
        self.nombre_jugador = str(nombre_jugador)           #Nombre de jugador
        self.enemigos_eliminados = str(enemigos_eliminados) #Enemigos eliminados
        self.velocidad_espada = str(velocidad)              #Velocidad de espada
        self.tiempo_partida = str(tiempo)                   #Tiempo transcurrido

        #CARGA LAS IMAGENES QUE SE USARÁN DENTRO DEL BOTÓN
        self.imagen_boton = pygame.image.load("assets/Menu/Boton.png")        #Imagen del botón
        self.imagen_personaje = pygame.image.load(imagen_personaje)   #Imagen Personaje
        self.imagen_espada = pygame.image.load("assets/Menu/espada_default.png")     #Imagen espada
        self.imagen_tiempo = pygame.image.load("assets/Menu/Imagen reloj.png")

        #DEFINE EL TAMAÑO DE LAS IMAGENES
        self.imagen_boton = pygame.transform.scale(self.imagen_boton, (430,125))   #Botón
        self.imagen_personaje = pygame.transform.scale(self.imagen_personaje, (130,130))    #Personaje
        self.imagen_espada = pygame.transform.scale(self.imagen_espada, (75,75))    #Espada
        self.imagen_tiempo = pygame.transform.scale(self.imagen_tiempo, (25, 25))   #Reloj


        #CREACIÓN DEL MARCO DE LAS IMAGENES
        self.imagen_boton_rect = self.imagen_boton.get_rect()           #marco del botón
        self.imagen_espada_rect = self.imagen_espada.get_rect()         #Marco de la espada
        self.imagen_personaje_rect = self.imagen_personaje.get_rect()   #Marco del personaje
        self.imagen_tiempo_rect = self.imagen_tiempo.get_rect()         #Imagen del reloj

        #POSICION DEL MARCO DE LA IMAGEN BOTON
        self.imagen_boton_rect.topleft = (x,y)

        #POSICIONAMIENTO DE LAS IMAGENES
        self.imagen_personaje_rect.left = self.imagen_boton_rect.left              #Lo posiciona en X
        self.imagen_personaje_rect.centery = self.imagen_boton_rect.centery - 25   #Lo centra en la posición Y

        self.imagen_espada_rect.left = self.imagen_boton_rect.left + 180    #Lo posiciona en X
        self.imagen_espada_rect.centery = self.imagen_boton_rect.centery + 19     #Lo centra en la posición Y

        self.imagen_tiempo_rect.left = self.imagen_boton_rect.left + 115       #Lo posiciona en X
        self.imagen_tiempo_rect.centery = self.imagen_boton_rect.centery + 10 #Lo centra en la posición Y

    def update(self):
        #Verifica la posición del mouse
        pos_mouse = pygame.mouse.get_pos()

        #Comprueba si el mouse está encima del botón
        if self.imagen_boton_rect.collidepoint(pos_mouse):
                self.hovered = True
                pass
        else:
            self.hovered = False

    def draw(self):
         #DIBUJA LAS IMAGENES USANDO (IMAGEN, MARCO DE LA IMAGEN)
         self.ventana.blit(self.imagen_boton, self.imagen_boton_rect)          #Imagen boton
         self.ventana.blit(self.imagen_personaje, self.imagen_personaje_rect)  #Imagen personaje
         self.ventana.blit(self.imagen_espada, self.imagen_espada_rect)       #Imagen espada
         self.ventana.blit(self.imagen_tiempo, self.imagen_tiempo_rect)        #Imagen reloj

         #CREA SUPERFICIES DE TEXTO
         self.texto_nombre = self.font.render(self.nombre_jugador, True,(255, 255, 255))  # Crea la superficie del texto con sus caracteristicas
         self.texto_tiempo = self.font.render(self.tiempo_partida, True,(200, 200, 200))  # Crea la superficie del texto con sus caracteristicas
         self.texto_espada = self.font.render(self.enemigos_eliminados, True,(200, 200, 200))

         #CREA LOS RECTS DEL TEXTO
         self.texto_nombre_rect = self.texto_nombre.get_rect()
         self.texto_tiempo_rect = self.texto_tiempo.get_rect()
         self.texto_espada_rect = self.texto_espada.get_rect()

         #POSICIONA LOS TEXTO
         self.texto_nombre_rect.left = self.imagen_boton_rect.left + 120
         self.texto_nombre_rect.centery = self.imagen_boton_rect.centery - 20

         self.texto_tiempo_rect.left = self.imagen_boton_rect.left + 150
         self.texto_tiempo_rect.centery = self.imagen_boton_rect.centery + 15

         self.texto_espada_rect.left = self.imagen_boton_rect.left + 235
         self.texto_espada_rect.centery = self.imagen_boton_rect.centery + 15

         #LOS DIBUJA
         self.ventana.blit(self.texto_nombre, self.texto_nombre_rect)
         self.ventana.blit(self.texto_tiempo, self.texto_tiempo_rect)
         self.ventana.blit(self.texto_espada, self.texto_espada_rect)