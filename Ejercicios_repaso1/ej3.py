def pintame(alto, ancho, car):
    for i in range(alto):
        print(car*ancho)

alto = int(input("ingrese el Alto:"))
ancho = int(input("ingrese el Ancho: "))
car = str(input("ingrese el caracter"))

pintame(alto, ancho, car)