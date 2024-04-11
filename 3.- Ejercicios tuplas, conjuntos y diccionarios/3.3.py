# Cristian Armando Larios Bravo 1ºD
""" 3.3.- Realiza un programa de forma libre en el que utilices algunos de los temas aprendidos como
 estructuras condicionales, funciones,  cadenas, listas, tuplas, diccionarios, notebooks, etc.  """

# Promedio de ventas de mayor mes en cadenas de alimentos y cuál ganó más

# MENÚ
print("\t .:::MENÚ:::.")
print("1. Las ganancias de Enero, Febrero y Marzo de las 3 cadenas de alimentos")
print("2. Calcular el promedio de ventas de cada cadena de alimentos de los 3 meses")
print("3. Calcular el promedio de ventas de las 3 cadenas de alimentos juntas")
print("4. Cual es la cadena con mejor ganancia de las 3 cadenas de alimentos y con cuanto ")
print("5. Salir")
opcion = int(input("Digite una opción del menú: "))

# Datos 
mcdonals = {'Enero':1250,'Febrero':976,'Marzo':1634}
burgerking = {'Enero':659,'Febrero':3821,'Marzo':1458}
pizzahut = {'Enero':1948,'Febrero':356,'Marzo':902}

# Funciones
def mayor3(a, b, c):
    if (a>b) & (a>c):
        return a
    elif (b>a) & (b>c):
        return b
    else:
        return c
def promedio(a,b,c):
    suma = a+b+c
    resultado = suma/3
    return resultado

# PROCESO
if opcion == 1:
    print("\t .:GANANCIAS DE ENERO, FEBERO Y MARZO:.")
    print(f"Mcdonals con {mcdonals}")
    print(f"Burger King con {burgerking}")
    print(f"Pizza Hut con {pizzahut}")
elif opcion == 2:
    print("\t .:PROMEDIO DE VENTAS DE CADA CADENA DE ALIMENTOS:.")
    
    a=tuple(mcdonals.values())     
    b=len(a)                      
    suma=0                                          # PROMEDIO DE VENTAS DE MCDONAL'S
    for val in a:                 
        suma+=val                  
        promedio1 = suma/b
    
    f=tuple(burgerking.values())     
    c=len(f)                      
    suma=0                                          # PROMEDIO DE VENTAS DE BURGER KING
    for val in f:                 
        suma+=val                  
        promedio2 = suma/c
    
    h=tuple(pizzahut.values())     
    d=len(h)                      
    suma=0                                          # PROMEDIO DE VENTAS DE PIZZA HUT
    for val in h:                 
        suma+=val                  
        promedio3 = suma/d

    print(f"McDonal's : ${promedio1}")
    print(f"Burger King : ${promedio2}")
    print(f"Pizza Hut : ${promedio3}")
elif opcion == 3:
    print("\t .:PROMEDIO DE VENTAS DE LAS 3 CADENAS DE ALIMENTOS JUNTAS:.")
    a=tuple(mcdonals.values())     
    b=len(a)                      
    suma=0                                          # PROMEDIO DE VENTAS DE MCDONAL'S
    for val in a:                 
        suma+=val                  
        promedio1 = suma/b
    
    f=tuple(burgerking.values())     
    c=len(f)                      
    suma=0                                          # PROMEDIO DE VENTAS DE BURGER KING
    for val in f:                 
        suma+=val                  
        promedio2 = suma/c
    
    h=tuple(pizzahut.values())     
    d=len(h)                      
    suma=0                                          # PROMEDIO DE VENTAS DE PIZZA HUT
    for val in h:                 
        suma+=val                  
        promedio3 = suma/d
    
    promedio_ganancias = promedio(promedio1,promedio2,promedio3)
    print(f"El promedio de ganancias de las 3 cadenas fue de ${promedio_ganancias:.2f}")
elif opcion == 4:
    print("\t .:CUAL ES LA CADENA CON MEJOR GANANCIA DE LAS 3 CADENAS DE ALIMENTOS Y CON CUANTO:.")
    a=tuple(mcdonals.values())     
    b=len(a)                      
    suma=0                                          # PROMEDIO DE VENTAS DE MCDONAL'S
    for val in a:                 
        suma+=val                  
        promedio1 = suma/b
    
    f=tuple(burgerking.values())     
    c=len(f)                      
    suma=0                                          # PROMEDIO DE VENTAS DE BURGER KING
    for val in f:                 
        suma+=val                  
        promedio2 = suma/c
    
    h=tuple(pizzahut.values())     
    d=len(h)                      
    suma=0                                          # PROMEDIO DE VENTAS DE PIZZA HUT
    for val in h:                 
        suma+=val                  
        promedio3 = suma/d
    
    mejor_ganancia = mayor3(promedio1,promedio2,promedio3)
    Sum = sum(f)
    print(f"La mejor ganancia fue de Burger King {burgerking} con: ${mejor_ganancia:.2f}(promedio)")
    print(f"Ganancia total de Burger King: ${Sum}")
elif opcion == 5:
    print("Saliendo del programa...")
else:
    print("Opción no válida")