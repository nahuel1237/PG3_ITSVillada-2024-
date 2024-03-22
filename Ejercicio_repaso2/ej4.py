class Operaciones:
    def __init__(self):
        self.num1 = int(input("Ingrese el numero 1: \n"))
        self.num2 = int(input("Ingrese el numero 2: \n"))
        self.suma()
        self.resta()
        self.multi()
        self.div()

    def suma(self):
        suma = self.num1 + self.num2
        print("Suma: ", suma)

    def resta(self):
        resta = self.num1 - self.num2
        print("Resta:", resta)

    def multi(self):
        multiplicacion = self.num1 * self.num2
        print("Multiplicacion: ", multiplicacion)

    def div(self):
        divicion = self.num1 / self.num2
        print("Divicion: ", divicion)

opreacion1 = Operaciones()