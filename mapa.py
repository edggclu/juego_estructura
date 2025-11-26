import pygame
import pytmx

from entidades.jugador import jugador

# Clase para el manejo del mapa
class Map:
    def __init__(self, archivo_tmx):
        # Cargar mapa
        mapa_tmx = pytmx.load_pygame(archivo_tmx, pixelalpha=True)

        # Dimensiones
        self.ancho_mapa = mapa_tmx.width * mapa_tmx.tilewidth
        self.alto_mapa = mapa_tmx.height * mapa_tmx.tileheight
        self.datos_mapa = mapa_tmx

    # Renderizado de capas y tiles
    def renderizar(self, superficie):
         for layer in self.datos_mapa.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                # Recorrido de tiles para dibujar
                for x, y , gid in layer:
                    tile = self.datos_mapa.get_tile_image_by_gid(gid)
                    if tile:
                        superficie.blit(tile, (x * self.datos_mapa.tilewidth,
                                                y * self.datos_mapa.tileheight))

    # Generacion de la superficie del mapa
    def crear_mapa(self):
        temporal_superficie = pygame.Surface((self.ancho_mapa, self.alto_mapa))
        self.renderizar(temporal_superficie)
        return temporal_superficie

    # Deteccion de tiles colindantes al jugador
    def get_piso(self, jugador):
        # Calculo de coordenadas en la pantalla
        xp = jugador.hitbox.x // 16 + 1 + abs(jugador.relative_x//16)
        yp = jugador.hitbox.y // 16 + 1 + abs(jugador.relative_y//16)

        # Retorno de identificadores de tiles adyacentes
        return  (self.datos_mapa.get_tile_gid(xp,yp-1, 1),
                 self.datos_mapa.get_tile_gid(xp+1,yp, 1),
                 self.datos_mapa.get_tile_gid(xp,yp+3, 1),
                 self.datos_mapa.get_tile_gid(xp-1,yp, 1))