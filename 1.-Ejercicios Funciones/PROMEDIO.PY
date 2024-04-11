#CRISTIAN ARMANDO LARIOS BRAVO 1ºD
#8.4.- Realiza un programa utilizando funciones que calcule el promedio de tres calificaciones de un estudiante. Pedirle al usuario las 3 calificaciones, en la función calcular y regresar(return) el promedio.
print("Bienvenido al programa que calcula el promdeio de tres calificaciones")
def promedio(a,b,c):
    suma = a+b+c
    resultado = suma/3
    return resultado

a = 0.0
b = 0.0
c = 0.0
a = float(input("Ingresa la primer calificación: "))
b = float(input("Ingresa la segunda calificación: "))
c = float(input("Ingresa la tercer calificación: "))
total = promedio(a, b, c)
print("El promedio de las 3 materias es: ",total)
