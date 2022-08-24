#Mostrar los numero pares comprendidos entre un valor inicial y un valor final de números
#enteros.
import os
clear = lambda: os.system('cls')
clear()

inicio = int(input("Primer numero: "))
final = int(input("Ultimo numero: "))

for inicio in range(final):
    inicio = inicio + 1
    if inicio %22 == 0:
       print(inicio)
