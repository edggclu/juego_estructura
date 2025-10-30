class partida:
    def __init__(self, ventana, tipo_personaje, arma):
        self.ventana = ventana
        self.arma = arma
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



