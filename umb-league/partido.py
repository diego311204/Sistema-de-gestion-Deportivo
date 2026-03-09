class Partido:

    def __init__(self, equipo1, equipo2):
        self.equipo1 = equipo1
        self.equipo2 = equipo2
        self.goles1 = 0
        self.goles2 = 0

    def registrar_resultado(self, g1, g2):

        self.goles1 = g1
        self.goles2 = g2

        self.equipo1.actualizar_estadisticas(g1, g2)
        self.equipo2.actualizar_estadisticas(g2, g1)

    def __str__(self):
        return f"{self.equipo1.nombre} vs {self.equipo2.nombre}"