import pygame
# El botón individual que representa una partida guardada
from ventanas.cargar_partida.clase_boton_cargar_partida import boton_cargar_partida
# El panel de la derecha que muestra los detalles de la partida seleccionada
from ventanas.cargar_partida.PanelInfoBase import PanelInfoBase
# El botón en la parte superior para seleccionar una forma de ordenamiento
from ventanas.cargar_partida.clase_boton_ordenamiento import BotonOrdenamiento
# La estructura de dato que contiene la lógica del algoritmo Insertion Sort
from ventanas.cargar_partida.insertion_sort import GestorOrdenamiento


class ventana_cargar_partida:

    #Representa la ventana principal (o escena) de cargar artida.

    #Qué gestiona:
    #1. La visualización del fondo.
    #2. La creación y posición de los botones de ordenamiento (TIME, GOLD, KILLS).
    #3. La creación y visualización de los botones de las partidas guardadas.
    #4. La lógica de ordenamiento al hacer clic en los botones de criterio.
    #5. La actualización del panel de detalles de la partida seleccionada (hovered).


    def __init__(self, ventana):
        #Inicializa la ventana de carga de partida y sus componentes

        # Define la superficie de la ventana
        self.ventana = ventana
        # Carga la imagen de fondo
        self.fondo = pygame.image.load('assets/Menu/Fondo.png')

        # Define el tamaño de la imagen de fondo para que se ajuste a la ventana
        self.fondo = pygame.transform.scale(self.fondo, (self.ventana.get_width(), self.ventana.get_height()))

        # DEFINIR BOTONES DE ORDENAMIENTO (CRITERIOS PARA USAR EN EL SORT)
        y_orden = 50  # Posición Y fija (Arriba de las partidas)
        x_orden = 50  # Posición X inicial
        espacio = 140 # Separación horizontal entre botones

        # Creación de instancias de los botones de ordenamiento
        self.btn_time = BotonOrdenamiento(self.ventana, x_orden, y_orden, "TIME", "assets/Menu/Imagen reloj.png")
        self.btn_gold = BotonOrdenamiento(self.ventana, x_orden + espacio, y_orden, "GOLD", "assets/Menu/bolsaDinero.png")
        self.btn_kills = BotonOrdenamiento(self.ventana, x_orden + espacio * 2, y_orden, "KILLS", "assets/Menu/EspadasCruzadas.png")

        # Lista de botones de ordenamiento para una mejor iteración
        self.lista_botones_orden = [self.btn_time, self.btn_gold, self.btn_kills]

        # Creamos el objeto que se encargará de ordenar / Instancia de la clase Gestor de ordenamiento
        self.gestor = GestorOrdenamiento()

        # CREACIÓN Y POSICIONAMIENTO DE LOS BOTONES
        pos_x = self.ventana.get_width() / 100 * 1  # 1% de la separación horizontal
        pos_y = 130                                # Posición Y inicial de la primera partida
        espaciado_partidas = 135                    # Separación vertical entre partidas

        # CREACION DE INSTANCIAS DE LOS BOTONES SEPARADOS
        # Nota: Los datos de tiempo, dinero, y kills se generan aleatoriamente dentro de la clase boton_cargar_partida
        self.boton1 = boton_cargar_partida(self.ventana, pos_x, pos_y, 21, "assets/Sprites/vampire_Base/Idle/sprite_0.png", "Luis miguel")
        self.boton2 = boton_cargar_partida(self.ventana, pos_x, pos_y + espaciado_partidas, 17, "assets/Sprites/skeleton_Base/Idle/skeleton_Base_Idle0.png", "Andresaurio espinoza")
        self.boton3 = boton_cargar_partida(self.ventana, pos_x, pos_y + espaciado_partidas * 2, 55, "assets/Sprites/skeleton_Base/Idle/skeleton_Base_Idle0.png", "Puñaron")
        self.boton4 = boton_cargar_partida(self.ventana, pos_x, pos_y + espaciado_partidas * 3, 12, "assets/Sprites/skeleton_Base/Idle/skeleton_Base_Idle0.png", "José José")

        # GUARDA LOS BOTONES EN UNA LISTA PAAR DESPUÉS PODER ORDENARLOS
        self.lista_partidas = [self.boton1, self.boton2, self.boton3, self.boton4]

        # Inicialmente, el panel muestra la información de la primera partida
        self.boton_info_actual = self.boton1

    def reorganizar_visuales(self):
        #Reposiciona verticalmente los botones de partida en pantalla
        #Se llama después de que se ha aplicado un ordenamiento a self.lista_partidas

        y_inicial = 130
        espaciado = 135
        for i, boton in enumerate(self.lista_partidas):
            # Calcula la nueva posición Y basada en el índice i en la lista ya ordenada
            nuevo_y = y_inicial + (i * espaciado)
            boton.mover_a_y(nuevo_y)

    def update(self):
        #Actualiza la lógica de la ventana y dibuja todos los elementos.
        # Dibujar el fondo primero
        self.ventana.blit(self.fondo, (0, 0))

        # Se obtiene la posición del mouse una sola vez al inicio del ciclo de update
        pos_mouse = pygame.mouse.get_pos()

        # Actualiza y dibuja los botones de orden
        for btn in self.lista_botones_orden:
            btn.update()
            btn.draw()

        # Lógica de ordenamiento (Clics en botones de orden)
        if pygame.mouse.get_pressed():  # Si se presiona el botón izquierdo del mouse
            se_ordeno = False

            # Verifica si el clic ocurrió en el área de cada botón de ordenamiento
            if self.btn_time.rect.collidepoint(pos_mouse):
                self.gestor.ordenar_por_tiempo(self.lista_partidas)
                se_ordeno = True
            elif self.btn_gold.rect.collidepoint(pos_mouse):
                self.gestor.ordenar_por_dinero(self.lista_partidas)
                se_ordeno = True
            elif self.btn_kills.rect.collidepoint(pos_mouse):
                self.gestor.ordenar_por_kills(self.lista_partidas)
                se_ordeno = True

            if se_ordeno:
                # Si se ejecutó un ordenamiento, se reposicionan visualmente los botones
                self.reorganizar_visuales()


        # Actualizar y dibujar botones de partida
        for boton in self.lista_partidas:
            boton.update()
            boton.draw()
            # Detectar el hover para actualizar el panel derecho
            if boton.hovered:
                self.boton_info_actual = boton  # El panel mostrará la info de este botón

        # Dibujar panel informativo
        self.Recuadro_informacion()

    def Recuadro_informacion(self):
        # Crea e instancia el panel de detalles para la partida actualmente seleccionada (hovered) y lo dibuja en la pantalla.
        # Se crea una nueva instancia de PanelInfoBase en cada ciclo de update, pasándole la referencia del botón cuya información
        # debe mostrar (self.boton_info_actual).
        panel_detalles = PanelInfoBase(self.ventana, self.boton_info_actual)
        panel_detalles.draw()