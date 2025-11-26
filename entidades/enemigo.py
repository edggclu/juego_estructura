import pygame
import random
from entidades.entidad import entidad

# Clase para la gestion de enemigos que hereda de entidad
class enemigo(entidad):
    def __init__(self, x, y, interfaz, nombre, jugador, arma):
        # Inicializacion de la clase padre
        super().__init__(x, y, interfaz, nombre, arma)
        self.jugador = jugador
        self.lista_actual_de_sprites = self.run_list

        self.delta_x = 0
        self.delta_y = 0

        # Cálculo del Campo de Visión (Inversamente proporcional)
        self.rango_vision = 1000 / max(1, self.velocidad)

        # Variables para el comportamiento de patrulla aleatoria
        self.ultimo_cambio_accion = pygame.time.get_ticks()
        self.tiempo_proxima_accion = random.randint(1000, 3000)  # Tiempo inicial aleatorio
        self.accion_actual = 'idle'  # 'idle' o 'run'
        self.direccion_patrulla = pygame.math.Vector2(0, 0)

    def mover(self):
        # Calculo de vectores y distancia respecto al jugador
        posicion_enemigo = pygame.math.Vector2(self.forma.center)
        posicion_jugador = pygame.math.Vector2(self.jugador.forma.center)

        # Vector hacia el jugador
        direccion = posicion_jugador - posicion_enemigo
        distancia = direccion.length()

        # Variable para saber si debemos movernos por lógica de IA (Perseguir o Patrullar)
        velocidad_ia = pygame.math.Vector2(0, 0)

        # Logica de persecucion si el jugador esta en rango
        if distancia < self.rango_vision:
            # Lógica de dirección y Flip basada en el JUGADOR
            if direccion[0] > 0:
                self.flip = False
            else:
                self.flip = True

            if not self.attack_action:
                # Verificacion de distancia para iniciar ataque
                if abs(direccion[0]) < 30 and abs(direccion[1]) < 33:
                    self.attack_action = True
                    self.steps = 0;
                    self.offset = 5;
                    self.contador_sprite = 0
                    self.lista_actual_de_sprites = self.attack_list
                else:
                    if self.lista_actual_de_sprites != self.death_list:
                        self.lista_actual_de_sprites = self.run_list
                        # Normalizamos para movernos hacia el jugador
                        if direccion.length() > 0:
                            direccion.normalize_ip()
                        velocidad_ia = direccion * self.velocidad

        # Logica de patrullaje cuando el jugador esta lejos
        else:
            tiempo_actual = pygame.time.get_ticks()

            # Control de tiempo para cambio de estado (Idle/Run)
            if tiempo_actual - self.ultimo_cambio_accion > self.tiempo_proxima_accion:
                self.ultimo_cambio_accion = tiempo_actual
                self.tiempo_proxima_accion = random.randint(1000, 3000)  # Nueva duración aleatoria

                # Decidir aleatoriamente entre quedarse quieto o caminar
                eleccion = random.choice(['idle', 'run'])
                self.accion_actual = eleccion

                if eleccion == 'run':
                    # Elegir dirección aleatoria
                    rand_x = random.uniform(-1, 1)
                    rand_y = random.uniform(-1, 1)
                    self.direccion_patrulla = pygame.math.Vector2(rand_x, rand_y)
                    if self.direccion_patrulla.length() > 0:
                        self.direccion_patrulla.normalize_ip()

            # Ejecutar la acción elegida
            if not self.attack_action and self.lista_actual_de_sprites != self.death_list:
                if self.accion_actual == 'run':
                    self.lista_actual_de_sprites = self.run_list
                    velocidad_ia = self.direccion_patrulla * (self.velocidad * 0.5)  # Patrullan más lento (50% vel)

                    # Flip basado en la dirección de patrulla
                    if self.direccion_patrulla.x > 0:
                        self.flip = False
                    else:
                        self.flip = True
                else:
                    self.lista_actual_de_sprites = self.idle_list
                    velocidad_ia = pygame.math.Vector2(0, 0)

        # Deteccion de colisiones y combate
        if direccion.length() > 0 and distancia < self.rango_vision:  # Normalizamos 'direccion' solo si se usará para empujes de combate
            direccion.normalize_ip()

        # Aplicacion de daño y empuje al jugador
        if self.hitbox_attack.colliderect(self.jugador.hitbox) and self.attack and not self.jugador.dano:
            golpe_x = direccion[0] * 60
            golpe_y = direccion[1] * 20
            self.jugador.dano = True
            self.jugador.forma.x += golpe_x
            self.jugador.forma.y += golpe_y
            self.jugador.vida -= 1
            self.jugador.update_camara()

        # Recepcion de daño por parte del jugador
        if self.hitbox.colliderect(self.jugador.hitbox_attack) and self.jugador.attack:
            self.vida -= self.jugador.fuerza
            # Empuje al recibir daño
            if direccion.length() > 0:  # Verificar para evitar error
                self.forma.x += direccion[0] * -50
            self.dano = True

        # Calculo del desplazamiento relativo a la camara (Scroll)
        movimiento_camara_x = 0
        movimiento_camara_y = 0

        if self.delta_x > self.jugador.relative_x:
            movimiento_camara_x = -self.jugador.velocidad
            self.delta_x = self.jugador.relative_x
        elif self.delta_x < self.jugador.relative_x:
            movimiento_camara_x = self.jugador.velocidad
            self.delta_x = self.jugador.relative_x

        if self.delta_y > self.jugador.relative_y:
            movimiento_camara_y = -self.jugador.velocidad
            self.delta_y = self.jugador.relative_y
        elif self.delta_y < self.jugador.relative_y:
            movimiento_camara_y = self.jugador.velocidad
            self.delta_y = self.jugador.relative_y

        # Aplicacion del movimiento final (IA + Scroll)
        if self.vida > 0:
            # Sumamos el vector de velocidad calculado arriba + el ajuste de camara
            self.forma.move_ip(velocidad_ia + (movimiento_camara_x, movimiento_camara_y))
        else:
            # Si muere, retroceso + cámara
            if distancia < self.rango_vision:  # Solo retrocede si el jugador estaba cerca
                self.forma.move_ip(direccion + (movimiento_camara_x, movimiento_camara_y))
            else:
                self.forma.move_ip((movimiento_camara_x, movimiento_camara_y))

        # Gestion de la muerte y cambio de sprites
        if self.vida <= 0:
            if self.lista_actual_de_sprites is not self.death_list:
                self.contador_sprite = 0
                self.lista_actual_de_sprites = self.death_list
                self.offset = 4