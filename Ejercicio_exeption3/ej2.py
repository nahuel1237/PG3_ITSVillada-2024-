while True:
    try:
        num1=int(input("ingrese el primer numero: \n>>"))
        num2=int(input("ingrese el segundo numero: \n>>"))
        div= num1 / num2
        print("la divicion es: ", div)
    
    except ValueError:
        print("Error, por favor ingrese un dato numerico")
    except ZeroDivisionError:
            print("Error, no se puede dividir por 0")

    finally:
        opcion= str(input("Queres seguir sumando (s/n): \n>>"))
        if opcion.lower() != "s":
            break
        