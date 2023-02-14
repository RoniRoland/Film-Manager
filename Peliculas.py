class peliculas:
    def __init__(self, nombre, actores, anio, genero):
        self.nombre = nombre
        self.actores = actores
        self.anio = anio
        self.genero = genero

    def mostrar_infopeli(self):
        print("\nNombre de la pelicula:", self.nombre, "\nActores principales:", self.actores,
              "\nAño de la pelicula:", self.anio, "\nGénero de la pelicula:", self.genero)
