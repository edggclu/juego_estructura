import pygame
import pytmx

class Map:
    def __init__(self, archivo_tmx):
        #Cargar mapa
        mapa_tmx = pytmx.load_pygame(archivo_tmx, pixelalpha=True)

        #Dimensiones
        self.ancho_mapa = mapa_tmx.width * mapa_tmx.tilewidth
        self.alto_mapa = mapa_tmx.height * mapa_tmx.tileheight
        self.datos_mapa = mapa_tmx

    def renderizar(self, superficie):
         for layer in self.datos_mapa.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y , gid in layer:
                    tile = self.datos_mapa.get_tile_image_by_gid(gid)
                    if tile:
                        superficie.blit(tile, (x * self.datos_mapa.tilewidth,
                                                y * self.datos_mapa.tileheight))

    def crear_mapa(self):
        temporal_superficie = pygame.Surface((self.ancho_mapa, self.alto_mapa))
        self.renderizar(temporal_superficie)
        return temporal_superficie