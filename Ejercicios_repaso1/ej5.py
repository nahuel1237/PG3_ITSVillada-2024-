def es_palindromo(palabra):

    palabra = palabra.lower()

    if palabra == palabra[::-1]:
        return True
    else:
        return False

palabra = input("ingrese la palabra: ")

if es_palindromo(palabra):
    print("La palabra '{}' es un palíndromo.".format(palabra))
else:
    print("La palabra '{}' no es un palíndromo.".format(palabra))