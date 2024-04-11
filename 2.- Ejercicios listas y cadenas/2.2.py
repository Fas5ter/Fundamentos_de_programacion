#CRISTIAN ARMANDO LARIOS BRAVO 1ºD
#2.2.- Realiza un programa que pida al usuario cuantos números quiere introducir. Luego leer todos los números y realizar una media aritmética.

contador, suma, numero = 0, 0, 1
while numero != 0:
    numero = float(input("Ingresa un número (0 para terminar): "))

    if numero != 0:
        suma += numero
        contador += 1
if contador == 0:
    print("No ingresaste ningun numero")
else:
    promedio= suma/contador

    print("El promedio de los {} numeros que ingresaste es igual a {}.".format(contador, promedio))