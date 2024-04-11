#CRISTIAN ARMANDO LARIOS BRAVO 1ºD
#2.5.- Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, pero no debe repetirse ningún elemento en la nueva lista.

x = [1,2,3,4,5,6]
y = [5,6,7,8,9,10]
r = x+y

repetidos = []
lista_sin_repeticiones = []

for n in r:
    if n not in lista_sin_repeticiones:
        lista_sin_repeticiones.append(n)
    else:
        repetidos.append(n)

print(lista_sin_repeticiones)