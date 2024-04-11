#CRISTIAN ARMANDO LARIOS BRAVO 1ºD
#2.1.- Realiza un programa que sume todos los números enteros pares desde el 0 hasta el 100.

numbers = []
for x in range(2,101,2):
    numbers.append(x)
Sum = sum(numbers)
print("El resultado de sumar todos los números enteros pares desde el 0 al 100 es ",Sum)