#CRISTIAN ARMANDO LARIOS BRAVO 1ºD
#8.1.- Realiza un programa utilizando funciones que compare 3 números y regrese (return) cuál es el mayor de los 3. 
print("Bienvenido al programa que compara 3 números y te dice cual es el mayor:")
def mayor3(a, b, c):
    if (a>b) & (a>c):
        return a
    elif (b>a) & (b>c):
        return b
    else:
        return c

a = 0
b = 0
c = 0
mayor = 0
a = int(input("Ingresa un número: "))
b = int(input("Ingresa el segundo número: "))
c = int(input("Ingresa el tercer número: "))
mayor = mayor3(a,b,c)
print("El número mayor es: ",mayor)