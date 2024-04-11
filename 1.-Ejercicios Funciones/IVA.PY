#CRISTIAN ARMANDO LARIOS BRAVO 1ºD
#8.2.- Realiza un programa utilizando funciones que calcule el IVA (16%) de una cantidad que el usuario proporcione, y sumársela. Es decir, calcular el precio más/con IVA. 
print("Bienvenido al programa que calcula el precio del producto mas el IVA")
def iva(a,b):
    resultado = a%b
    return resultado

a = 16
b = 0
b = float(input("Introduce el precio del producto: "))
total_iva = iva(a,b)
suma = total_iva+b
print("El precio del producto mas el IVA es: ",suma)

