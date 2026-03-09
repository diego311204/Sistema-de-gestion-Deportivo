class Presupuesto:

    def __init__(self, monto):

        self.monto_total = monto
        self.monto_usado = 0

    def solicitar_apoyo(self, costo):

        if self.monto_usado + costo <= self.monto_total:

            self.monto_usado += costo
            return True

        else:
            return False


    def disponible(self):

        return self.monto_total - self.monto_usado