#
# 3. Aplicar el IVA al precio de un producto.
import os
clear = lambda: os.system('cls')
clear()

print("-"*20)
print("<<Cajero>>")
print("-"*20)

product = str(input("Nombre del producto: "))
precio = float(input("Precio del producto: "))

iva = precio * 0.15
precio = precio + iva

print("-"*20)

print("Se aplica el 15% de IVA")

print(f"Total a pagar {precio}")
