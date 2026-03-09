from gestor import Gestor


def menu():

    gestor = Gestor()

    while True:

        print("\nUMB LEAGUE MANAGER")
        print("1. Registrar equipo")
        print("2. Generar torneo")
        print("3. Registrar resultado")
        print("4. Tabla de posiciones")
        print("5. Solicitar apoyo")
        print("6. Campeón")
        print("0. Salir")

        op = input("Seleccione: ")

        if op == "1":
            gestor.registrar_equipo()

        elif op == "2":
            gestor.torneo.generar_enfrentamientos()

        elif op == "3":
            gestor.registrar_resultado()

        elif op == "4":
            gestor.torneo.tabla_posiciones()

        elif op == "5":
            gestor.solicitar_apoyo()

        elif op == "6":
            gestor.torneo.campeon()

        elif op == "0":
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu()