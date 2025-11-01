import os

import pygame

class ventana_nueva_partida:
    def __init__(self, ventana):
        self.ventana = ventana
        self.fondo = pygame.image.load('ventanas/menu/Fondo.png')
        self.fondo = pygame.transform.scale(self.fondo, (self.ventana.get_width(), self.ventana.get_height()))
        self.fase = 1
        self.boton = pygame.image.load('ventanas/menu/Boton.png')
        self.armas_stats = [
                self.crear_arma("Default", 3, 3, 0),
                self.crear_arma("Rojo", 5, 2, 0),
                self.crear_arma("Azul", 2, 5, 0),
                self.crear_arma("Verde", 1, 3, 1),
            ]
        self.boton_rect = self.boton_rect2 = None
        self.lista_jugadores = ["Skeleton1", "Vampire_Brown"]
        self.botones_jugadores = [self.boton_rect, self.boton_rect2]

        self.contador_sprite = 0
        self.offset = 3
        self.listas_sprites = (self.cargar_sprites("Skeleton1/Idle"), self.cargar_sprites("Vampire_Brown/Idle"))
        self.sprites_para_animar = [self.listas_sprites[0][0], self.listas_sprites[1][0]]
        self.steps_list = [0,2]
        self.img_para_rect = pygame.image.load('assets/Sprites/Skeleton1/Idle/idle_00.png')
        self.type = None




    def update(self):
        self.ventana.fill((0, 0, 0))
        self.ventana.blit(self.fondo, (0, 0))
        if self.fase == 1:
            self.fase_1()
        elif self.fase == 2:
            self.fase_2()

    def fase_1(self):
        boton1 = pygame.image.load('ventanas/menu/BaseMenu.png')
        boton1 = pygame.transform.scale(boton1, (400, 400))

        self.boton_rect = pygame.Rect(0, 0, boton1.get_width(), boton1.get_height())
        self.boton_rect.x = self.ventana.get_width()/2 - 450
        self.boton_rect.y = self.ventana.get_height() / 2 - self.boton_rect.height / 2

        self.boton_rect2 = pygame.Rect(0, 0, boton1.get_width(), boton1.get_height())
        self.boton_rect2.x = self.ventana.get_width()/2 + 50
        self.boton_rect2.y = self.ventana.get_height() / 2 - self.boton_rect.height / 2

        self.ventana.blit(boton1, self.boton_rect)
        self.ventana.blit(boton1, self.boton_rect2)
        self.botones_jugadores = [self.boton_rect, self.boton_rect2]

        m = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.boton_rect.collidepoint(m):
            pygame.mouse.set_cursor(pygame.cursors.ball)
            if click[0] == 1:
                self.fase = 2
                self.type = "Skl"
                pygame.mouse.set_cursor(pygame.cursors.arrow)
        elif self.boton_rect2.collidepoint(m):
            pygame.mouse.set_cursor(pygame.cursors.ball)
            if click[0] == 1:
                self.fase = 2
                self.type = "Vamp"
                pygame.mouse.set_cursor(pygame.cursors.arrow)
        else:
            pygame.mouse.set_cursor(pygame.cursors.arrow)


        for i in range(len(self.lista_jugadores)):
            im = self.img_para_rect
            image_rect = im.get_rect()
            image_rect.x = self.botones_jugadores[i].x + 40
            image_rect.y = self.botones_jugadores[i].y - 50
            self.ventana.blit(self.sprites_para_animar[i], image_rect)

        self.animar()

    def fase_2(self):
        for i in range(0, 4):
            boton1 = pygame.image.load('ventanas/menu/BaseMenu.png')
            boton1 = pygame.transform.scale(boton1, (200, 200))

            self.boton_rect = pygame.Rect(0, 0, boton1.get_width(), boton1.get_height())
            self.boton_rect.x = 65 + 250*i
            self.boton_rect.y = self.ventana.get_height() / 2 - self.boton_rect.height / 2


            self.ventana.blit(boton1, self.boton_rect)


    def nueva_partida(self):
        pass

    def crear_arma(self,color, dano, velocidad, veneno):
        arma = {
            color:{
                "Fuerza": dano,
                "Velocidad": velocidad,
                "Veneno": veneno
            }
        }
        return arma

    def animar(self):
        pygame.display.set_caption(f'{self.type}')
        if self.contador_sprite == self.offset:
            self.steps_list[1] += 1
            self.steps_list[0] += 1
            if self.steps_list[0] >= len(self.listas_sprites[0])-1:
                self.steps_list[0] = 0
            if self.steps_list[1] >= len(self.listas_sprites[1]) - 1:
                self.steps_list[1] = 0
            self.sprites_para_animar[0] = self.listas_sprites[0][self.steps_list[0]]
            self.sprites_para_animar[1] = self.listas_sprites[1][self.steps_list[1]]

            self.contador_sprite = 0
        self.contador_sprite += 1


    def cargar_sprites(self, path):
        dir = f'assets/Sprites/' + path
        list = os.listdir(dir)
        for i in range(len(list)):
            im = (pygame.image.load(dir + "/" +list[i]).convert_alpha())
            list[i] =(pygame.transform.scale(im, (400,400)))
        return list
