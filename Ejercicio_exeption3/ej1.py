while True:
    try:
        num1=int(input("ingrese el primer numero: \n>>"))
        num2=int(input("ingrese el segundo numero: \n>>"))
        suma= num1 + num2
        print("la suma es: ", suma)
    
    except ValueError:
        print("Error, por favor ingrese un dato numerico")

    finally:
        opcion= str(input("Queres seguir sumando (s/n): \n>>"))
        if opcion.lower() != "s":
            break
        