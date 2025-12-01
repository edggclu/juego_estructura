import pygame
import sys
from entidades.enemigo import enemigo
from entidades.jugador import jugador
from mapa import Map
import random


class ventana_juego:
    def __init__(self, ventana, partida):
        self.ventana = ventana
        self.partida = partida

        # ESTADOS Y MENÚ
        self.estado = 'jugando'
        self.fuente = pygame.font.SysFont('minecraft', 30)
        self.fuente_stats = pygame.font.SysFont('minecraft', 20)

        self.opciones_pausa = ["Continuar jugando", "Salir"]
        self.seleccion_pausa = 0

        # Crea el mapa
        self.mapa_juego = Map("assets/mapa/mapa2.tmx")
        self.fondo_mapa = self.mapa_juego.crear_mapa()

        # LÓGICA EN INGLÉS
        self.lista_colores = ['Base', 'Blue', 'Green', 'Red']
        self.lista_tipo_enemigos = ['skeleton', 'vampire']

        # Diccionario de estadísticas (Claves en inglés)
        self.stats = {}
        for tipo in self.lista_tipo_enemigos:
            for color in self.lista_colores:
                clave = f"{tipo}_{color}"
                self.stats[clave] = 0

        # Diccionario para traducir
        self.traducciones = {
            'skeleton': 'Esqueleto',
            'vampire': 'Vampiro',
            'Base': 'Base',
            'Blue': 'Azul',
            'Green': 'Verde',
            'Red': 'Rojo'
        }

        self.jugador = jugador(ventana.get_width() / 2,
                               ventana.get_height() / 2,
                               ventana,
                               f'{self.partida.tipo_personaje}',
                               self.partida.arma,
                               self.mapa_juego)

        # Armas
        self.armas_stats = [
            self.crear_arma("Base", 3, 3, 0),
            self.crear_arma("Blue", 1, 3, 0),
            self.crear_arma("Green", 1, 3, 1),
            self.crear_arma("Red", 5, 2, 0),
        ]

        # Spawner
        self.ultimo_spawn = pygame.time.get_ticks()
        self.tiempo_proximo_spawn = random.randint(1000, 3000)

        self.entidades = [self.jugador]
        #self.agregar_enemigo(20, 20, 'skeleton', 'Blue')

    def update(self):
        # --- 1. PROCESAR EVENTOS ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                self.jugador.key_down(event)

                if event.key == pygame.K_ESCAPE:
                    if self.estado == 'jugando':
                        self.estado = 'pausa'
                    else:
                        self.estado = 'jugando'

                if self.estado == 'pausa':
                    if event.key == pygame.K_UP:
                        self.seleccion_pausa = (self.seleccion_pausa - 1) % len(self.opciones_pausa)
                    elif event.key == pygame.K_DOWN:
                        self.seleccion_pausa = (self.seleccion_pausa + 1) % len(self.opciones_pausa)
                    elif event.key == pygame.K_RETURN:
                        if self.seleccion_pausa == 0:
                            self.estado = 'jugando'
                        elif self.seleccion_pausa == 1:
                            pygame.quit()
                            sys.exit()
            if event.type == pygame.KEYUP:
                self.jugador.key_up(event)

        # DIBUJADO DE LA VENTANA
        self.ventana.fill((0, 0, 0))
        x = self.jugador.relative_x
        y = self.jugador.relative_y
        self.ventana.blit(self.fondo_mapa, (x, y))

        # LÓGICA SEGÚN ESTADO
        if self.estado == 'jugando':
            tiempo_actual = pygame.time.get_ticks()
            if len(self.entidades) < 11:
                if tiempo_actual - self.ultimo_spawn > self.tiempo_proximo_spawn:
                    tipo = random.choice(self.lista_tipo_enemigos)
                    color = random.choice(self.lista_colores)
                    px = random.randint(50, self.ventana.get_width() - 50)
                    py = random.randint(50, self.ventana.get_height() - 50)

                    self.agregar_enemigo(px, py, tipo, color)
                    self.ultimo_spawn = tiempo_actual
                    self.tiempo_proximo_spawn = random.randint(1000, 5000)

            self.jugador.gid_lados = self.mapa_juego.get_piso(self.jugador)
            for entidad in self.entidades:
                if entidad.vivo:
                    entidad.update()

            # Conteo de bajas
            for entidad in self.entidades:
                if not entidad.vivo:
                    if entidad != self.jugador:
                        if hasattr(entidad, 'nombre') and entidad.nombre in self.stats:
                            self.stats[entidad.nombre] += 1
                    self.entidades.remove(entidad)

            self.dibujar_stats()

        elif self.estado == 'pausa':
            self.dibujar_stats()
            self.mostrar_menu_pausa()

    # IMPLEMENTACIÓN DE QUICKSORT
    def quicksort_stats(self, lista):
        # Caso base
        if len(lista) <= 1:
            return lista

        # Eleccion del pivote
        pivot = lista[len(lista) // 2]
        valor_pivot = pivot[1]  # Cantidad de kills

        # Partición de la lista
        izquierda = [x for x in lista if x[1] > valor_pivot]
        medio = [x for x in lista if x[1] == valor_pivot]
        derecha = [x for x in lista if x[1] < valor_pivot]

        # Llamada recursiva
        return self.quicksort_stats(izquierda) + medio + self.quicksort_stats(derecha)

    # Dibuja los stats
    def dibujar_stats(self):
        titulo = self.fuente_stats.render("Enemigos Matados (Quicksort):", True, (255, 255, 0))
        rect_titulo = titulo.get_rect(topright=(self.ventana.get_width() - 10, 10))
        self.ventana.blit(titulo, rect_titulo)

        offset_y = 35

        # Convertimos el diccionario a lista de tuplas para poder ordenarlo
        lista_items = list(self.stats.items())

        # LLAMADA AL ALGORITMO QUICKSORT
        lista_ordenada = self.quicksort_stats(lista_items)

        # Iteramos sobre la lista YA ORDENADA
        for clave_ingles, cantidad in lista_ordenada:

            if cantidad > 0:
                # 1. Separamos nombre
                tipo_ing, color_ing = clave_ingles.split('_')

                # 2. Traducimos
                tipo_esp = self.traducciones.get(tipo_ing, tipo_ing)
                color_esp = self.traducciones.get(color_ing, color_ing)

                # 3. Construimos texto
                cadena = f"{tipo_esp} {color_esp}: {cantidad}"

                texto_render = self.fuente_stats.render(cadena, True, (255, 255, 255))
                rect_texto = texto_render.get_rect(topright=(self.ventana.get_width() - 10, 10 + offset_y))
                self.ventana.blit(texto_render, rect_texto)

                offset_y += 20

    def mostrar_menu_pausa(self):
        s = pygame.Surface((self.ventana.get_width(), self.ventana.get_height()))
        s.set_alpha(150)
        s.fill((0, 0, 0))
        self.ventana.blit(s, (0, 0))

        for i, texto in enumerate(self.opciones_pausa):
            color = (255, 255, 255) if i == self.seleccion_pausa else (150, 150, 150)
            prefix = "> " if i == self.seleccion_pausa else ""

            render = self.fuente.render(prefix + texto, True, color)
            rect = render.get_rect(center=(self.ventana.get_width() // 2, self.ventana.get_height() // 2 + i * 40))
            self.ventana.blit(render, rect)

    def agregar_enemigo(self, x, y, tipo, color):
        stats = self.armas_stats[self.lista_colores.index(color)]
        self.entidades.append(enemigo(x, y, self.ventana, f'{tipo}_{color}', self.jugador, stats))

    def crear_arma(self, color, dano, velocidad, Curacion):
        return {color: {"Fuerza": dano, "Velocidad": velocidad, "Curacion": Curacion}}