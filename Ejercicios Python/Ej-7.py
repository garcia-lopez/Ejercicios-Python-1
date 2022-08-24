#Leer x cantidad de edades y mostrar el promedio de dichas edades.

import os
clear = lambda: os.system('cls')
clear()

cant = int(input("Cantidad de edades << "))

suma = 0
for i in range(cant):
    edad = int(input(f"Edad {i + 1} >> "))
    suma += edad

promedio = suma / cant

print(f"El promedio de edades es >>{promedio} ")
     
