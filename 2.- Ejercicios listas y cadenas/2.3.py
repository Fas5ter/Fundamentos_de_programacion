#CRISTIAN ARMANDO LARIOS BRAVO 1ºD
#2.3.- Realiza un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso. 
#Luego debe comprobar si el número se encuentra en la lista de números y notificarlo. 
#Inicia con: numeros = [1, 3, 6, 9]

lista = [1, 3, 6 ,9]
valor = int(input("Ingresa un número entero del 0 al 9: "))
if valor in lista:
    print("El numero ",valor," si se encuentra en la lista")
else:
    "El número no se encuentra en la lista"

