
def encontrarMayor ():
    n = int(input("Ingresa un número:"))
    mayor = 0
    while n != -1:
        if n > mayor:
            mayor = n
        n = int(input("Ingresa un número [-1 para salir]: "))
    print("El número mayor es: ", mayor)

def dividir ():
    D = int(input("Dividendo: "))
    d = int(input("Divisor: "))
    cociente = 0
    while D>0:
        cociente = cociente + 1
        D = D - d
    if D != 0:
        cociente = cociente - 1
        residuo = d + D
    print(cociente)
    print(residuo)

def main ():
    n = False
    while n != True:
        print("Misión 07. Ciclos While")
        print("Autor: Roberto Castro Barrios")
        print("Matrícula: A01748559")
        print("1. Calcular Divisiones")
        print("2. Encontrar el mayor")
        print("3. Salir")
        n = int(input("Tecla tu opción: "))
        if n == 1:
            encontrarMayor()
        elif n == 2:
            dividir()
        elif n == 3:
            n = True
main()


