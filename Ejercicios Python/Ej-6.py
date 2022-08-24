#Leer dos números y decir cual es mayor y cual es menor.
import os
clear = lambda: os.system('cls')
clear()

num1 = int(input("Digite el primer numero entero: "))
num2 = int(input("Digite el segundo numero entero: "))

if num1 < num2:
    print(f"{num2} es mayor")
    print(f"{num1} es menor")
else: 
    print(f"{num1} es mayor")
    print(f"{num2} es menor")