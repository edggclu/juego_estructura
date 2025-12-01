import random
import pygame

class boton_cargar_partida:

    # Representa un botón individual de partida guardada en la ventana de carga, contiene la información
    # de la partida y es interactivo.

    def __init__(self, ventana, x, y, tiempo, imagen_personaje, nombre_jugador):
        #Inicializa un botón de partida con sus datos y elementos gráficos.

        #Paramtros usados:
        # ventana: La superficie principal de Pygame.
        # x: Posición X inicial del botón.
        # y: Posición Y inicial del botón.
        # tiempo: Tiempo de partida inicial
        # imagen_personaje: Ruta de la imagen base del personaje
        # nombre_jugador: El nombre de la partida/jugador.

        pygame.font.init()                                 # Inicializa el módulo de fuente
        self.font = pygame.font.Font(None, 24)   # Usa la fuente por defecto, tamaño 24
        self.ventana = ventana
        self.hovered = False                               # Estado de hover del mouse

        # GENERACIÓN DE ESTADÍSTICAS ALEATORIAS
        # Conteo de Esqueletos (Aleatorio entre 0 y 100)
        self.kills_esqueleto_base = (random.randint(0, 100))
        self.kills_esqueleto_azul = (random.randint(0, 100))
        self.kills_esqueleto_verde = (random.randint(0, 100))
        self.kills_esqueleto_rojo = (random.randint(0, 100))

        # Conteo de Vampiros (Aleatorio entre 0 y 100)
        self.kills_vampiro_base = (random.randint(0, 100))
        self.kills_vampiro_azul = (random.randint(0, 100))
        self.kills_vampiro_verde = (random.randint(0, 100))
        self.kills_vampiro_rojo = (random.randint(0, 100))


        # DATOS DE TEXTO PARA MOSTRAR
        self.nombre_jugador = str(nombre_jugador)

        # Cálculo de kills totales, convertido a string para su visualización
        self.enemigos_eliminados = str(self.kills_vampiro_azul + self.kills_vampiro_base + self.kills_vampiro_rojo +
                                       self.kills_vampiro_verde + self.kills_esqueleto_verde + self.kills_esqueleto_azul
                                       + self.kills_esqueleto_base + self.kills_esqueleto_rojo)

        self.tiempo_partida = (str(tiempo) + " minutos") # Tiempo de partida, convertido a string con unidad
        self.dinero_acumulado = str(random.randint(0, 999)) # Dinero aleatorio, convertido a string

        self.ruta_imagen_personaje = imagen_personaje # Ruta usada para mostrar en el botón y en PanelInfoBase

        # CARGA Y ESCALADO DE IMÁGENES DE COMPONENTES
        self.imagen_boton = pygame.image.load("assets/Menu/Boton.png")
        self.imagen_personaje = pygame.image.load(imagen_personaje)
        self.imagen_espada = pygame.image.load("assets/Menu/espada_default.png")
        self.imagen_tiempo = pygame.image.load("assets/Menu/Imagen reloj.png")
        self.imagen_bolsaDinero = pygame.image.load("assets/Menu/bolsaDinero.png")

        # ESCALADO
        self.imagen_boton = pygame.transform.scale(self.imagen_boton, (430, 125))
        self.imagen_personaje = pygame.transform.scale(self.imagen_personaje, (130, 130))
        self.imagen_espada = pygame.transform.scale(self.imagen_espada, (75, 75))
        self.imagen_tiempo = pygame.transform.scale(self.imagen_tiempo, (25, 25))
        self.imagen_bolsaDinero = pygame.transform.scale(self.imagen_bolsaDinero, (25, 25))


        # OBTENCIÓN DE RECTÁNGULOS DE POSICIÓN
        self.imagen_boton_rect = self.imagen_boton.get_rect()
        self.imagen_espada_rect = self.imagen_espada.get_rect()
        self.imagen_personaje_rect = self.imagen_personaje.get_rect()
        self.imagen_tiempo_rect = self.imagen_tiempo.get_rect()
        self.imagen_bolsaDinero_rect = self.imagen_bolsaDinero.get_rect()

        # POSICIÓN INICIAL DEL BOTÓN PRINCIPAL
        self.imagen_boton_rect.topleft = (x, y)

        # POSICIONAMIENTO INICIAL RELATIVO A imagen_boton_rect
        self.imagen_personaje_rect.left = self.imagen_boton_rect.left
        self.imagen_personaje_rect.centery = self.imagen_boton_rect.centery - 22

        self.imagen_espada_rect.left = self.imagen_boton_rect.left + 230
        self.imagen_espada_rect.centery = self.imagen_boton_rect.centery + 19

        self.imagen_tiempo_rect.left = self.imagen_boton_rect.left + 115
        self.imagen_tiempo_rect.centery = self.imagen_boton_rect.centery + 10

        self.imagen_bolsaDinero_rect.left = self.imagen_boton_rect.left + 330
        self.imagen_bolsaDinero_rect.centery = self.imagen_boton_rect.centery + 10

    def update(self):
        #Actualiza la lógica del botón, principalmente para detectar si el mouse está encima (hover).

        pos_mouse = pygame.mouse.get_pos()

        # Comprueba si el mouse está encima del botón principal
        if self.imagen_boton_rect.collidepoint(pos_mouse):
                self.hovered = True
                pass
        else:
            self.hovered = False

    def draw(self):

        # Dibuja el botón, sus iconos y sus textos en la ventana.

        # Dibujar Fondo y Personaje
        # La posición del personaje debe recalcularse para seguir al botón,
        # ya que el botón puede haberse movido por el ordenamiento.
        self.imagen_personaje_rect.left = self.imagen_boton_rect.left
        self.imagen_personaje_rect.centery = self.imagen_boton_rect.centery - 25

        self.ventana.blit(self.imagen_boton, self.imagen_boton_rect)
        self.ventana.blit(self.imagen_personaje, self.imagen_personaje_rect)

        # Renderizar Textos ya que el texto no es estático
        self.texto_nombre = self.font.render(self.nombre_jugador, True, (255, 255, 255))
        self.texto_tiempo = self.font.render(self.tiempo_partida, True, (200, 200, 200))
        self.texto_espada = self.font.render(self.enemigos_eliminados, True, (200, 200, 200))
        self.texto_BolsaDinero = self.font.render(self.dinero_acumulado, True, (200, 200, 200))

        # Obtener los rectángulos de los textos
        self.texto_nombre_rect = self.texto_nombre.get_rect()
        self.texto_tiempo_rect = self.texto_tiempo.get_rect()
        self.texto_espada_rect = self.texto_espada.get_rect()
        self.texto_BolsaDinero_rect = self.texto_BolsaDinero.get_rect()

        # POSICIONAMIENTO Y DIBUJADO DE TEXTOS E ICONOS

        # TEXTO NOMBRE
        self.texto_nombre_rect.left = self.imagen_personaje_rect.right - 30
        self.texto_nombre_rect.centery = self.imagen_boton_rect.centery - 20
        self.ventana.blit(self.texto_nombre, self.texto_nombre_rect)

        # TIEMPO (ICONO - TEXTO)
        self.imagen_tiempo_rect.left = self.imagen_personaje_rect.right - 30
        self.imagen_tiempo_rect.centery = self.imagen_boton_rect.centery + 10
        self.ventana.blit(self.imagen_tiempo, self.imagen_tiempo_rect)

        self.texto_tiempo_rect.left = self.imagen_tiempo_rect.right + 8
        self.texto_tiempo_rect.centery = self.imagen_boton_rect.centery + 15
        self.ventana.blit(self.texto_tiempo, self.texto_tiempo_rect)

        # ESPADA (ICONO - TEXTO)
        self.imagen_espada_rect.left = self.texto_tiempo_rect.right
        self.imagen_espada_rect.centery = self.imagen_boton_rect.centery + 20
        self.ventana.blit(self.imagen_espada, self.imagen_espada_rect)

        self.texto_espada_rect.left = self.imagen_espada_rect.right - 20
        self.texto_espada_rect.centery = self.imagen_boton_rect.centery + 10
        self.ventana.blit(self.texto_espada, self.texto_espada_rect)

        # DINERO (ICONO - TEXTO)
        self.imagen_bolsaDinero_rect.left = self.texto_espada_rect.right + 30
        self.imagen_bolsaDinero_rect.centery = self.imagen_boton_rect.centery + 10
        self.ventana.blit(self.imagen_bolsaDinero, self.imagen_bolsaDinero_rect)

        self.texto_BolsaDinero_rect.left = self.imagen_bolsaDinero_rect.right + 5
        self.texto_BolsaDinero_rect.centery = self.imagen_boton_rect.centery + 10
        self.ventana.blit(self.texto_BolsaDinero, self.texto_BolsaDinero_rect)

    # MÉTODOS PARA ORDENAMIENTO (Usados por GestorOrdenamiento)
    def obtener_tiempo_int(self):
        # Elimina la parte de texto " minutos" y convierte el número a entero
        return int(self.tiempo_partida.split(" ")[0])

    def obtener_dinero_int(self):
        #Extrae y retorna el valor numérico del dinero acumulado como un entero.
        return int(self.dinero_acumulado)

    def obtener_kills_int(self):
        #Extrae y retorna el valor numérico de las kills totales como un entero
        return int(self.enemigos_eliminados)

    def mover_a_y(self, nueva_y):
        # Reposiciona el botón verticalmente, usado después de un ordenamiento
        # Parametro usado:
        # nueva_y: La nueva coordenada Y top para el botón.
        self.imagen_boton_rect.top = nueva_y