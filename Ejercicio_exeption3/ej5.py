"""
Almacenar una serie de string en un archivo de texto. Tratar de llamar al método 'write' pasando un 
entero. Capturar la excepcion correspondiente
"""

#funcion para escribir un archivo
def escribir_en_archivo():
    #intentamos
    try:
        #creamos el archivo de texto de tipo escritura
        with open("texto.txt", "w") as archivo:
            archivo.write("Hola")
            texto = ""
            archivo.write(texto)
        print("Operación de escritura completada.")
    #error si escribe un valor numerico
    except TypeError as e:
        print("Error:", e)
        print("Se esperaba una cadena de texto. No se pudo escribir el entero.")
    #mostramos el error
    except Exception as e:
        print("Ocurrió un error:", e)

#llamamos a la funcion
escribir_en_archivo()
