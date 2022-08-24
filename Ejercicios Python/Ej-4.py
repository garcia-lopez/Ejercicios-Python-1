#4. Calcular la edad de una persona.
import os
clear = lambda: os.system('cls')
clear()

print("Calculadora de edad")

print("-"*20)
dianac = int(input("Dia de nacimiento: "))
print("1- Enero")
print("2- Febrero")
print("3- Marzo")
print("4- Abril")
print("5- Mayo")
print("6- Junio")
print("7- Julio")
print("8- Agosto")
print("9- Septiembre")
print("10- Octubre")
print("11-Noviembre")
print("12-Diciembre")
print("-"*20)

mesnac = int(input("Mes de naciemiento: "))

añonac = int(input("Año de nacimiento: "))

print("-"*20)

diact = int(input("Dia de hoy: "))

print("-"*20)
print("1- Enero")
print("2- Febrero")
print("3- Marzo")
print("4- Abril")
print("5- Mayo")
print("6- Junio")
print("7- Julio")
print("8- Agosto")
print("9- Septiembre")
print("10- Octubre")
print("11-Noviembre")
print("12-Diciembre")
mesact = int(input("Mes de naciemiento: "))
print("-"*20)

añoact = int(input("Año actual: "))

edad = añoact -añonac

if mesnac == mesact:
    if dianac > diact:
        edad = edad - 1
else: 
  if mesnac > mesact:
    edad = edad - 1

print(f"Su edad es = {edad}")

