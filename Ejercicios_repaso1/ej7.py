def step(num):

    numero_str = str(num)

    for i in range(1, len(numero_str)):
        if int(numero_str[i]) != int(numero_str[i - 1]) + 1:
            return False
    return True
num = input("ingrese un numero: ")

if step(num):
    print("el numero es step")
else:
    print("el numero no es step")