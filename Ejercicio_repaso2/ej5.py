class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir(self):
        print("Hola ",self.nombre, "Edad ", self.edad)


class Empleado(Persona):

    def __init__(self,sueldo, nombre, edad):
        super().__init__(nombre = nombre, edad = edad)
        self.sueldo = sueldo
        self.imprimir()
        self.impuestos()
    def impuestos(self):
        if self.sueldo>=3000:
            print("Debe pagar impuestos")
        else:
            print("no debe pagar impuestos")

    def imprimir(self):
        print(f"Nombre: {self.nombre} Edad: {self.edad} Sueldo: {self.sueldo}")


persona1 = Persona("Miguel", 25)
empleado1 = Empleado(3500 , "Miguel", 25)


