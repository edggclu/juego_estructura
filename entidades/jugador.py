import pygame
from entidades.entidad import entidad


# Clase del Jugador Principal que hereda de entidad
class jugador(entidad):
    def __init__(self, x, y, interfaz, nombre, arma, mapa):
        # Inicializacion de la clase padre y ajustes de velocidad
        super().__init__(x, y, interfaz, nombre, arma)
        self.velocidad += 1

        # Banderas de control de movimiento
        self.mover_arriba = False
        self.mover_abajo = False
        self.mover_derecha = False
        self.mover_izquierda = False
        self.attack_action = False

        self.piso = 0

        self.idle = True
        self.flip = False

        # Configuracion de vida y hitbox
        # self.vida = 25
        self.vof = self.hitbox.width / self.vida
        self.gid_lados = (0, 0, 0, 0)

        # self.hitbox_attack = pygame.rect.Rect((self.hitbox.centerx + (self.hitbox.width/2 * 1.6)),self.hitbox.y +40,40,self.hitbox.height + 10)
        self.attack = False
        self.color_vida = (0, 255, 0)

        # Variables de camara y limites del mapa
        self.delta_y = self.delta_x = 0
        self.mapa = mapa
        self.relative_x = self.relative_y = 0
        self.max_world_x = (self.mapa.datos_mapa.width * 16) - self.interfaz.get_width()
        self.max_world_y = (self.mapa.datos_mapa.height * 16) - self.interfaz.get_height()

    def mover(self):
        # Reinicio de los vectores de movimiento por frame
        self.delta_x = 0
        self.delta_y = 0

        # Establece el delta segun la tecla presionada
        if self.mover_derecha:
            self.delta_x = self.velocidad
        if self.mover_izquierda:
            self.delta_x = -self.velocidad
        if self.mover_arriba:
            self.delta_y = -self.velocidad
        if self.mover_abajo:
            self.delta_y = self.velocidad

        # Establece el arreglo de animaciones segun la accion
        if not self.attack_action:
            if self.delta_x > 0: self.lista_actual_de_sprites = self.run_list; self.flip = False
            if self.delta_x < 0: self.lista_actual_de_sprites = self.run_list; self.flip = True
            if self.delta_y != 0: self.lista_actual_de_sprites = self.run_list;
            if self.delta_x == 0 == self.delta_y: self.lista_actual_de_sprites = self.idle_list
            self.attack = False
        else:
            self.lista_actual_de_sprites = self.attack_list
            # if 1 < self.steps < len(self.lista_actual_de_sprites) - 1:
            #    self.attack = True

        # Bloqueo de movimiento en caso de colision con tiles
        if self.gid_lados[0] != 0 and self.delta_y == -self.velocidad:
            self.delta_y = 0
        if self.gid_lados[1] != 0 and self.delta_x == self.velocidad:
            self.delta_x = 0
        if self.gid_lados[2] != 0 and self.delta_y == self.velocidad:
            self.delta_y = 0
        if self.gid_lados[3] != 0 and self.delta_x == -self.velocidad:
            self.delta_x = 0

        # Mueve la camara del personaje con el mapa
        self.update_camara()

        # pygame.display.set_caption(f'{(self.relative_x, self.relative_y)}')

        # Actualizacion final de la posicion
        self.forma.x += self.delta_x
        self.forma.y += self.delta_y

    # Logica de Scrolling de la camara
    def update_camara(self):
        # Condicion de la derecha
        if self.interfaz.get_width() - self.hitbox.right < 100 and self.delta_x == self.velocidad:
            if self.relative_x <= 0:
                self.relative_x -= self.delta_x
                # self.hitbox.right = self.interfaz.get_width() - 100
            # No avanza el personaje hasta llegar al limite, solo avanza la pantalla
            if self.relative_x + self.max_world_x >= 0:
                self.delta_x = 0

        # Condicion Izquierda
        if self.hitbox.left <= 100 and self.delta_x == -self.velocidad:
            if self.relative_x < 0:
                self.hitbox.left = 100
                self.relative_x -= self.delta_x
                self.delta_x = 0

        # Condicion Arriba
        if self.hitbox.top <= 100 and self.delta_y == -self.velocidad:
            if self.relative_y < 0:
                self.relative_y -= self.delta_y
                self.delta_y = 0

        # Condicion Abajo
        if self.interfaz.get_height() - self.hitbox.bottom < 100 and self.delta_y == self.velocidad:
            if self.relative_y <= 0:
                self.relative_y -= self.delta_y

            if self.relative_y + self.max_world_y >= 0:
                self.delta_y = 0

        # Restriccion de la camara a los limites maximos del mapa
        if self.relative_x < -self.max_world_x:
            self.relative_x = -self.max_world_x
        if self.relative_x > 0:
            self.relative_x = 0
        if self.relative_y < -self.max_world_y:
            self.relative_y = -self.max_world_y
        if self.relative_y > 0:
            self.relative_y = 0

    # Manejo de eventos al presionar teclas
    def key_down(self, event):
        if event.key == pygame.K_w: self.mover_arriba = True
        if event.key == pygame.K_a: self.mover_izquierda = True
        if event.key == pygame.K_d: self.mover_derecha = True
        if event.key == pygame.K_s: self.mover_abajo = True
        if event.key == pygame.K_n: self.vida -= 1
        if not self.attack_action:
            if event.key == pygame.K_j: self.attack_action = True;  self.steps = 0; self.offset = 15 // self.velocidad; self.contador_sprite = 0

    # Manejo de eventos al soltar teclas
    def key_up(self, event):
        if event.key == pygame.K_w: self.mover_arriba = False
        if event.key == pygame.K_a: self.mover_izquierda = False
        if event.key == pygame.K_d: self.mover_derecha = False
        if event.key == pygame.K_s: self.mover_abajo = False