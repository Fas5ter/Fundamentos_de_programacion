#CRISTIAN ARMANDO LARIOS BRAVO 1ºD
#8.5.- Realiza un programa utilizando funciones que pida al usuario 2 números, y permita al usuario elegir entre alguna de las operaciones de suma, resta, división y multiplicación. El programa debe contener 4 funciones: suma, resta, multiplicación y división.
print("Bienvenido al programa que pide dos números y te permite sumar, restar, multiplicar o dividir esos dos numeros")
def suma(x, y):
    resultado = x+y
    return resultado

def resta(x, y):
    resultado = x-y
    return resultado

def division(x, y):
    resultado = x/y
    return resultado

def multiplicacion(x, y):
    resultado = x*y
    return resultado

x = 0
y = 0
opc = " "
total = 0

x = float(input("Escribe un número: "))
y = float(input("Escribe el segundo número: "))
opc = input("Ingresa la operación que deseas realizar, s: Suma, r: Resta, d: División, m: Multiplicación ")

if opc == "s":
    total = suma(x, y)
    print("El resultado de la suma es: ",total)
elif opc == "r":
    total = resta(x, y)
    print("El resultado de la resta es: ",total)
elif opc == "d":
    total = division(x, y)
    print("El resultado de la división es: ",total)
elif opc == "m":
    total = multiplicacion(x, y)
    print("El resultado de la multiplicación es: ",total)
else:
    print("No introduciste una operación válida")