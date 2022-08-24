"""9. Leer los datos de un estudiante como el nombre, los apellidos, la carrera y su promedio.
Evaluar si apto para beca, el estudiante podrá optar a beca si su promedio es mayor a 85
en todas las carreras excepto Ingeniería de Sistemas donde su promedio debe ser mayor a
95."""

import os
clear = lambda: os.system('cls')
clear()

print("-"*20)

print("<< Registro >>")

nombre1 = str(input("Primer nombre >> "))
nombre2 = str(input("Segundo nombre >> "))
apellido1 = str(input ("Primer apellido >> "))
apellido2 = str(input ("Segundo apellido >> "))

promedio = float(input("Promedio de final 5to año >> "))
print("-"*20)

print("-"*20)
print("<< Carreras >>")

print("1- Administración de Empresas")
print("2- Arquitectura")
print("3- Contabilidad")
print("4- Diseño Gráfico")
print("5- Enseñanza del idioma Inglés")
print("6- Económia")
print("7- Ing. Ambiental")
print("8- Ing. Civil")
print("9- Ing. Industrial")
print("10- Ing. Sistemas")

carrera = int(input("Carrera seleccionada >> "))
print("-"*20)

if carrera == 10:
    if promedio >= 95:
        print("Califica para una beca")
    else:
        print("No califica para una beca")
else:
    if promedio >= 85:
        print("Califica para una beca")
    else:
        print("No Califica para una beca")

print("-"*20)
print("Datos almacenados correctamente")
print(f"Nombres: {nombre1.upper()} - {nombre2.upper()}")
print(f"Apellidos: {apellido1.upper()} - {apellido2.upper()}")

print("Carrera:")
if carrera == 1:
        print("Administracion de Empresas")
elif carrera == 2:            
        print("Arquitectura")
elif carrera == 3:
        print("Contabilidad")
elif carrera == 4:
        print("Diseño Gráfico")
elif carrera == 5:
        print ("Enseñanza del idioma Inglés")
elif carrera == 6:
        print ("Economia")
elif carrera == 7:
        print ("Ing. Ambiental")
elif carrera == 8:
        print("Ing. Civil")
elif carrera == 9:
        print ("Ing. Industrial")
elif carrera == 10:
        print ("Ing. Sistemas")


