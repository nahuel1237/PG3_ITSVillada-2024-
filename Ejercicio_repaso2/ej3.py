class Triangulo:

    def __init__(self):
        self.lado1 = int(input("Ingrese el lado 1: \n"))
        self.lado2 = int(input("Ingrese el lado 2: \n"))
        self.lado3 = int(input("Ingrese el lado 3: \n"))

    def lado_mayor(self):
        if self.lado1>self.lado2 and self.lado1> self.lado3:
            print("El lado mayor es", self.lado1)

        if self.lado2 > self.lado1 and self.lado1 > self.lado3:
            print("El lado mayor es", self.lado2)

        if self.lado3 > self.lado2 and self.lado3 > self.lado1:
            print("El lado mayor es", self.lado3)

    def equilatero(self):
        if self.lado1 == self.lado2 == self.lado3:
            print("El triangulo es equilatero")
        else:
            print("El triangulo no es equilatero")

triangulo = Triangulo()
triangulo.lado_mayor()
triangulo.equilatero()