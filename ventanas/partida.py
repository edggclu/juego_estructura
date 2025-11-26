import ast

# Clase de gestion de partida
class partida:
    def __init__(self , tipo_personaje, arma:dict):
        # Conversion de string a estructura de datos (diccionario)
        self.arma = ast.literal_eval(arma)
        self.tipo_personaje = tipo_personaje

        # Inicializacion de estadisticas de enemigos
        self.estadisticas = {
            "Esqueletos":{
                "Defaults": 0,
                "Rojos": 0,
                "Azules": 0,
                "Verdes": 0
            },
            "Vampiros":{
                "Defaults": 0,
                "Rojos": 0,
                "Azules": 0,
                "Verdes": 0
            }
        }