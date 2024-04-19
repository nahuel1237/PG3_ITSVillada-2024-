while True:
    meses = ["enero", "febrero", 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
    try:
        a = int(input('Ingrese el número del mes: \n>>'))
        if a < 1 or a > 12:
            raise IndexError
        print('El mes es:', meses[a - 1])
    except IndexError:
        print('El número ingresado no corresponde a un mes del año.')
    finally:
        opcion = input("¿Quieres seguir participando? (s/n): \n>>")
        if opcion.lower() != "s":
            break
