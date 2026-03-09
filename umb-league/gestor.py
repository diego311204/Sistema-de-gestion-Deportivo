from equipo import Equipo
from torneo import Torneo
from presupuesto import Presupuesto


class Gestor:

    def __init__(self):

        self.torneo = Torneo()
        self.presupuesto = Presupuesto(1000000)


    def registrar_equipo(self):

        nombre = input("Nombre del equipo: ")

        if nombre.strip() == "":
            print("Nombre inválido")
            return

        equipo = Equipo(nombre)
        self.torneo.registrar_equipo(equipo)

        print("Equipo registrado correctamente")


    def registrar_resultado(self):

        self.torneo.mostrar_partidos()

        while True:
            try:
                i = int(input("Seleccione partido: ")) - 1

                if i < 0 or i >= len(self.torneo.partidos):
                    print("Número inválido")
                    continue

                break

            except ValueError:
                print("Debe ingresar un número válido")

        while True:
            try:
                g1 = int(input("Goles equipo 1: "))
                break
            except ValueError:
                print("Número inválido")

        while True:
            try:
                g2 = int(input("Goles equipo 2: "))
                break
            except ValueError:
                print("Número inválido")

        self.torneo.partidos[i].registrar_resultado(g1, g2)

        print("Resultado registrado correctamente")


    def solicitar_apoyo(self):

        while True:

            try:

                costo = int(input("Costo solicitado: "))

                if costo <= 0:
                    print("El costo debe ser mayor que 0")
                    continue

                break

            except ValueError:

                print("Número inválido. Ingrese un número entero")

        if self.presupuesto.solicitar_apoyo(costo):

            print("Apoyo aprobado")
            print("Presupuesto restante:", self.presupuesto.disponible())

        else:

            print("Presupuesto insuficiente")