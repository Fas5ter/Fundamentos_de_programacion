#CRISTIAN ARMANDO LARIOS BRAVO 1ºD
#2.7.- Al realizar una consulta en un registro hemos obtenido una cadena de texto corrupta al revés. Al parecer contiene el nombre de un alumno y la nota de un examen. ¿Cómo podríamos formatear la cadena y conseguir una estructura como la siguiente?: ha sacado un de nota.

cadena = "zeréP nauJ,01"
print(cadena[9::-1],"ha sacado un",cadena[12:]+cadena[11:12],"de nota")