<h1 align = 'center'> 
  Proyecto Final Estructura | Juego de Hordas 
</h1>

<p align="center" >
     <img width="100" heigth="100" src="https://imgs.search.brave.com/6P9y7g4EsmZrWWoZN8PrG1N8w7WIii8AMPb9jDacfVo/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly91cGxv/YWQud2lraW1lZGlh/Lm9yZy93aWtpcGVk/aWEvY29tbW9ucy9j/L2MzL1B5dGhvbi1s/b2dvLW5vdGV4dC5z/dmc">
</p>


Este proyecto consiste en un videojuego 2D desarrollado con Python y Pygame, cuyo enfoque académico principal es demostrar la implementación y aplicación de dos algoritmos de ordenamiento clásicos:
- **Insertion Sort**, utilizado para ordenar partidas guardadas.
- **Quicksort**, utilizado para ordenar estadísticas en tiempo real al momento de jugar.

## El juego permite al usuario:
- Navegar por un menú principal con botones animados.
- Crear una nueva partida, seleccionando personaje (Esqueleto o Vampiro) y un arma/color con estadísticas específicas.
- Entrar al modo de juego, donde el jugador se mueve por un mapa TMX, se enfrenta a enemigos y acumula kills.
- Acceder a la ventana de cargar partida, con información detallada y reordenamiento dinámico según distintos criterios.
- Visualizar estadísticas de enemigos eliminados ordenadas en tiempo real.

El proyecto está estructurado con programación orientada a objetos, dividiendo cada ventana, entidad y elemento interactivo en su propia clase. Utiliza pytmx para cargar mapas diseñados en Tiled y pygame.Rect para detectar colisiones y manejar movimiento.

### Librerias Externas Utilizadas:
 - [pygame](https://www.pygame.org/news)
 - [pytmx](https://pypi.org/project/PyTMX/)

Asegúrate de tener instalado Python 3.13. Luego, instala las librerías necesarias con el comando:
```python
pip install . . .
```
## Ejecutar el juego

En la terminal, dentro de la carpeta del proyecto o correr el archivo main.py desde el editor/ide:
```python
python main.py
```

## Controles básicos
- Mouse -> Navegación por menús
- W / A / S / D -> Movimiento del jugador
- ESC -> Pausa
- Ataque -> Tecla J

## Sorts:
**Ordenamiento de partidas con Insertion Sort**
Implementado en GestorOrdenamiento.
Ordena las partidas de forma visual en pantalla.
Se actualiza dinámicamente al presionar:
- Botón TIME
- Botón GOLD
- Botón KILLS
Motivo del uso de Insertion Sort:
Las listas son pequeñas (3–6 elementos).
Es estable.
Fácil de implementar.
Perfecto para listas cortas y UI interactiva.
Registro interno de cuántos enemigos se han derrotado.

**Ordenamiento mediante Quicksort:**
Visualización de estadísticas en pantalla.
Las estadísticas (skeleton_Blue, vampire_Base, etc.) se ordenan por kills en orden descendente.
Implementado en ventana_juego.quicksort_stats().
