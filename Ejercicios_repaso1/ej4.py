def ordenar_numeros(entrada):

    numeros = [int(numero) for numero in entrada.split()]
    numeros_ordenados = sorted(numeros)
    return numeros_ordenados


entrada = input("Ingrese los números separados por espacios: ")
print("Números ordenados:", ordenar_numeros(entrada))