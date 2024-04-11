#CRISTIAN ARMANDO LARIOS BRAVO 1ºD
#8.3.- Realiza un programa utilizando funciones que calcule el factorial de un número. 
print("Bienvenido al programa que calcula el factorial de un numero")
def fact(n):
    factorial_total = 1
    while n > 1:
        factorial_total *= n
        n -= 1
    return factorial_total

num = int(input("Introduce un número: "))
total = fact(num)
print("El factorial del número",num,"es",total)
