def contar_vocales(frase):
    vocales = ['a', 'e', 'i', 'o', 'u']
    contador_vocales = 0
    for caracter in frase:
        if caracter in vocales:
            contador_vocales += 1
    return contador_vocales



frase = input("Ingrese una frase para contar las vocales: ")


print("Cantidad de vocales en la frase: ", contar_vocales(frase))