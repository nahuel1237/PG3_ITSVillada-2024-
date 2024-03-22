class Alumno:
    def inicializar(self, nom, nota):
        self.nombre = nom
        self.nota = nota

    def nota_regular(self):
        if self.nota > 4:
            print("Estado: Regular")
        else:
            print("Estado: Libre")

    def imprimir(self):
        print("Nombre:", self.nombre, " Nota: ", self.nota)

alumno1 = Alumno()
alumno1.inicializar("Juan", 9)
alumno1.imprimir()
alumno1.nota_regular()

alumno2 = Alumno()
alumno2.inicializar("Martin", 2)
alumno2.imprimir()
alumno2.nota_regular()

