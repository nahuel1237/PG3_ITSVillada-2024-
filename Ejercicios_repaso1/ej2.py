
def anio_bisiesto(anio):
    if anio%4 == 0:
        if anio % 100 == 0:
            if anio % 400 == 0:
                return  True
            else:
                return False
        else:
            return  True
    else:
        return False


anio = int(input("ingrese un año: "))
if anio_bisiesto(anio):
    print("el año es bisiesto")
else:
    print("el año no es bisiesto")