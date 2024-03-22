class Familia:
    def __init__(self):
        self.padre = input("Ingrese el nombre del padre: ")
        self.madre = input("Ingrese el nombre de la madre: ")
        hijos = int(input("ingrese la cantidad de hijos: "))
        self.hijo = []
        for i in range(hijos):
            h = str(input("ingrese el nombre del hijo:"))
            self.hijo+=h
        self.imprimir()

    def imprimir(self):
        print(f"Padre: {self.padre} Madre: {self.madre} Hijos: {self.hijo}")

familia1 = Familia()
