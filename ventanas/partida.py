import ast

class partida:
    def __init__(self , tipo_personaje, arma:dict):
        self.arma = ast.literal_eval(arma)
        self.tipo_personaje = tipo_personaje

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



