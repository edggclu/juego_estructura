class ventana_nueva_partida:
    def __init__(self, ventana):
        self.ventana = ventana
        self.armas_stats = [
                self.crear_arma("Default", 3, 3, 0),
                self.crear_arma("Rojo", 5, 2, 0),
                self.crear_arma("Azul", 2, 5, 0),
                self.crear_arma("Verde", 1, 3, 1),
            ]

    def update(self):
        pass
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

