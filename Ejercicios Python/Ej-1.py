#. Mostrar el total a pagar por la compra de n cantidad de productos a un precio
#desconocido.
import os
clear = lambda: os.system('cls')
clear()

print("<< Cajero automático >>")

print("*"*50)

producto = str(input("Nombre del producto: "))
ncant = int(input(f"Cantidad de unidades de {producto.upper()}: "))
precio = float(input(f"Precio individual de {producto.upper()}: "))

print("*"*50)

total = ncant * precio 


print(f"Total a pagar << {total} << por la compra de << {ncant} << unidades de << {producto.upper()} <<")
print("*"*50)
