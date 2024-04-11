# Cristian Armando Larios Bravo 1ºD
'''3.2.- Realiza un programa que siga las siguientes instrucciones:
a) Crea un diccionario materia con las siguientes claves y valores: {'Sandra':10, 'Juan':9, 'Alejandro':8, 'Cristina':7, 'Jorge':6}
b) Muestra al usuario un menú con las siguientes opciones, para las cuales utilizarás funciones:
   - Agregar alumno, 
   - Eliminar alumno, 
   - Modificar calificación, 
   - Consulta (Recorre y muestra el diccionario, incluyendo la clave y su valor. ),
   - Promedio (Obtener el promedio de calificaciones.),
   - Salir.'''

materia = {'Sandra':10, 'Juan':9, 'Alejandro':8, 'Cristina':7, 'Jorge':6}
# MENÚ
print("\t .:MENÚ:.")
print("1. Agregar alumno") 
print("2. Eliminar alumno") 
print("3. Modificar calificación") 
print("4. Consulta (Recorre y muestra el diccionario, incluyendo la clave y su valor.")
print("5. Promedio (Obtener el promedio de calificaciones.)")
print("6. Salir.")
opcion = int(input("Digite una opcion del menú: "))
print()
# PROCESO
if opcion==1:
   n = input("Ingresa el nombre del alumno: ")
   y = int(input("Ingresa la calificación del alumno: "))
   materia[n] = y
   print("La nueva lista de alumnos y calificaciones es: ")
   for clave, valor in materia.items():
    print(clave,"|",valor)
elif opcion==2:
   n = input("Ingresa el nombre del alumno: ")
   del(materia[n])
   print("La nueva lista de alumnos y calificaciones es: ")
   for clave, valor in materia.items():
    print(clave,"|",valor)
elif opcion==3:
   n = input("Ingresa el nombre del alumno: ")
   y = int(input("Ingresa la nueva calificación del alumno: "))
   materia[n] = y
   print("La nueva lista de alumnos y calificaciones es: ")
   for clave, valor in materia.items():
    print(clave,"|",valor)
elif opcion==4:
   print("La lista de alumnos y calificaciones es: ")
   for clave, valor in materia.items():
    print(clave,"|",valor)
elif opcion==5:
   a=tuple(materia.values())     # Para agarrar todos los valores
   b=len(a)                      # Para agarrar cuantos valores hay
   suma=0                        # Contador
   for val in a:                 # Función for
      suma+=val                  # Suma de todos los valores
   print("El promedio es: ",suma/b)    # Imprimir la suma de los valores entre cuantos valores hay
elif opcion==6:
   print("Saliendo del programa...")
else:
   print("Opcion no válida")