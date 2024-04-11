# Cristian Armando Larios Bravo 1ºD
'''3.1.- Realiza un programa que siga las siguientes instrucciones en ese orden:

a) Crear un conjunto llamado usuarios con los usuarios Ana, David, Laura, Juan y Daniel
b) Crear un conjunto llamado administradores con los administradores Juan y Ana.
c) Borra al administrador Juan del conjunto de administradores.
d) Añadir a Daniel como un nuevo administrador, pero no lo borres del conjunto de usuarios.
e) Mostrar todos los usuarios por pantalla de forma dinámica, además debes indicar cada usuario es administrador o no.'''

usuarios = {"Ana","Daniel","Laura","Juan","David"}
administradores = {"Juan","Ana"}
administradores.discard("Juan")
administradores.add("Daniel")

print("\t.:ADMINISTRADORES Y USUARIOS:.")
x = {"Ana":"Administrador","Daniel":"Administrador","Laura":"Usuario","Juan":"Usuario","David":"Usuario"}
for clave, valor in x.items():
    print(clave,":",valor)