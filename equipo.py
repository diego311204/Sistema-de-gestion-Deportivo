class Equipo:

    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = 0
        self.partidos_jugados = 0
        self.goles_favor = 0
        self.goles_contra = 0

    def actualizar_estadisticas(self, gf, gc):

        self.partidos_jugados += 1
        self.goles_favor += gf
        self.goles_contra += gc

        if gf > gc:
            self.puntos += 3

        elif gf == gc:
            self.puntos += 1


    def __str__(self):

        return f"{self.nombre} | Pts:{self.puntos} PJ:{self.partidos_jugados}"