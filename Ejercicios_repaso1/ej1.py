
lista = [1,2,3,4,5,6,7,8]

def buscar(lista, num):
    for i in range(len(lista)):
        if lista[i] == num:
            return i
    return None

print("ingrese el numero a buscar:")
num = int(input())

indice = buscar(lista, num)
if indice is not None:
    print("el elemento buscado esta en", indice)

else:
    print("el numero no se encuentra en la lista")