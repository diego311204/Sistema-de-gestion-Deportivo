from partido import Partido

class Torneo:

    def __init__(self):
        self.equipos = []
        self.partidos = []
        self.grupoA = []
        self.grupoB = []

    def registrar_equipo(self, equipo):
        self.equipos.append(equipo)

    # Generar torneo estilo mundial
    def generar_enfrentamientos(self):

        if len(self.equipos) < 8:
            print("Se necesitan mínimo 8 equipos para un torneo tipo mundial")
            return

        # Crear grupos
        self.grupoA = self.equipos[:4]
        self.grupoB = self.equipos[4:8]

        print("\n===== GRUPO A =====")
        for e in self.grupoA:
            print(e.nombre)

        print("\n===== GRUPO B =====")
        for e in self.grupoB:
            print(e.nombre)

        print("\n===== PARTIDOS GRUPO A =====")
        self.generar_partidos_grupo(self.grupoA)

        print("\n===== PARTIDOS GRUPO B =====")
        self.generar_partidos_grupo(self.grupoB)


    # Generar partidos dentro de cada grupo
    def generar_partidos_grupo(self, grupo):

        for i in range(len(grupo)):
            for j in range(i+1, len(grupo)):

                partido = Partido(grupo[i], grupo[j])
                self.partidos.append(partido)

                print(grupo[i].nombre, "vs", grupo[j].nombre)


    def mostrar_partidos(self):

        if len(self.partidos) == 0:
            print("No hay partidos generados")
            return

        print("\nPARTIDOS DEL TORNEO")

        for i, p in enumerate(self.partidos):
            print(f"{i+1}. {p.equipo1.nombre} vs {p.equipo2.nombre}")


    def tabla_posiciones(self):

        tabla = sorted(self.equipos, key=lambda x: x.puntos, reverse=True)

        print("\nTABLA DE POSICIONES")

        for e in tabla:
            print(e)


    def campeon(self):

        tabla = sorted(self.equipos, key=lambda x: x.puntos, reverse=True)

        if tabla:
            print("\nEl campeón es:", tabla[0].nombre)