
import pygame
class boton_cargar_partida:

    def __init__(self, ventana,x,y, imagen_personaje, imagen_espada, velocidad, daño_espada,  nombre_jugador):
        pygame.font.init()  #Modulo fuente para los textos
        self.font = pygame.font.Font(None, 24)  # Fuente por defecto, tamaño 24

        #CARGA LAS IMAGENES QUE SE USARÁN DENTRO DEL BOTÓN
        self.imagen_boton = pygame.image.load("ventanas/menu/Boton.png")        #Imagen del botón
        self.imagen_personaje = pygame.image.load(imagen_personaje)   #Imagen Personaje
        self.imagen_espada = pygame.image.load(imagen_espada)     #Imagen espada

        #DEFINE EL TAMAÑO DE LAS IMAGENES
        self.imagen_boton = pygame.transform.scale(self.imagen_boton, (430,125))   #Botón
        self.imagen_personaje = pygame.transform.scale(self.imagen_personaje, (50,50))    #Personaje
        self.imagen_espada = pygame.transform.scale(self.imagen_espada, (50,50))    #Espada

        self.ventana = ventana

        #CREACIÓN DEL MARCO DE LAS IMAGENES
        self.imagen_boton_rect = self.imagen_boton.get_rect()           #marco del botón
        self.imagen_espada_rect = self.imagen_espada.get_rect()              #Marco de la espada
        self.imagen_personaje_rect = self.imagen_personaje.get_rect()   #Marco del personaje

        #POSICION DEL MARCO DE LA IMAGEN BOTON
        self.imagen_boton_rect.topleft = (x,y)

        #POSICIONAMIENTO DE LAS IMAGENES
        self.imagen_personaje_rect.left = self.imagen_boton_rect.left + 20
        self.imagen_personaje_rect.centery = self.imagen_boton_rect.centery   #Lo centra en la posición Y

        self.imagen_espada_rect.left = self.imagen_personaje_rect.right + 10
        self.imagen_espada_rect.centery = self.imagen_boton_rect.centery      #Lo centra en la posición Y

        #TEXTOS A USAR EN EL BOTÓN
        self.nombre_jugaror = str(nombre_jugador)   #Nombre de jugaro
        self.daño_espada = str(daño_espada)         #Daño de espada
        self.velocidad_espada = str(velocidad)      #Velocidad de espada

    def update(self):
        #Verifica la posición del mouse
        pos_mouse = pygame.mouse.get_pos()

        #Comprueba si el mouse está encima del botón
        if self.imagen_boton_rect.collidepoint(pos_mouse):
                #Código para la animacion del personaje si el mouse está encima del botón
                pass

    def draw(self):
         #DIBUJA LAS IMAGENES USANDO (IMAGEN, MARCO DE LA IMAGEN)
         self.ventana.blit(self.imagen_boton, self.imagen_boton_rect)          #Imagen boton
         self.ventana.blit(self.imagen_personaje, self.imagen_personaje_rect)  #Imagen personaje
         self.ventana.blit(self.imagen_espada, self.imagen_espada_rect)        #Imagen espada

         #COLOCA EL TEXTO
         texto_surface = self.font.render(self.nombre_jugaror, True, (255, 255, 255))   #Crea la superficie del texto con sus caracteristicas
         texto_rect = texto_surface.get_rect()                                          #Guarda el marco del texto en una variable
         texto_rect.left = self.imagen_espada_rect.right + 15                           #Posiciona la X del marco del texto
         texto_rect.centery = self.imagen_boton_rect.centery                            #Posiciona la Y del marco del texto
         self.ventana.blit(texto_surface, texto_rect)                                   #Dibuja la imagen/marco del texto