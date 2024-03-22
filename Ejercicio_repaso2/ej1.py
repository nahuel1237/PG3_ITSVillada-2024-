class Persona:

    def inicializar(self, nom):
        self.nombre = nom

    def imprimir(self):
        print("El nombre es: ", self.nombre)

persona1 = Persona()
persona1.inicializar("Santiago")
persona1.imprimir()

persona2 = Persona()
persona2.inicializar("Mateo")
persona2.imprimir()