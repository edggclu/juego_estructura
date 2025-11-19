class GestorOrdenamiento:
    # Clase que contiene la lógica del algoritmo insertion sort

    def ordenar_por_tiempo(self, lista_botones):
        return self._aplicar_insertion_sort(lista_botones, self._criterio_tiempo)

    def ordenar_por_dinero(self, lista_botones):
        return self._aplicar_insertion_sort(lista_botones, self._criterio_dinero)

    def ordenar_por_kills(self, lista_botones):
        return self._aplicar_insertion_sort(lista_botones, self._criterio_kills)

    # CRITERIOS
    def _criterio_tiempo(self, boton):
        return boton.obtener_tiempo_int()
    def _criterio_dinero(self, boton):
        return boton.obtener_dinero_int()
    def _criterio_kills(self, boton):
        return boton.obtener_kills_int()

    # ALGORITMO INSERTION SORT
    def _aplicar_insertion_sort(self, lista, funcion_criterio):
        for i in range(1, len(lista)):
            boton_actual = lista[i]
            valor_actual = funcion_criterio(boton_actual)
            j = i - 1

            while j >= 0:
                boton_comparado = lista[j]
                valor_comparado = funcion_criterio(boton_comparado)

                if valor_comparado < valor_actual:
                    lista[j + 1] = lista[j]
                    j -= 1
                else:
                    break
            lista[j + 1] = boton_actual
        return lista