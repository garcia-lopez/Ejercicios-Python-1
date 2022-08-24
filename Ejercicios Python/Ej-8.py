#Leer x cantidad de precios y mostrar el precio mas alto y el precio más bajo.
import os
clear = lambda: os.system('cls')
clear()

precios = []
bucle = 1
while(bucle == 1):   
    try:         
      precio = int(input("Precio del producto >> "))
      precios.append(precio)
      bucle = int(input("Agregar otro precio 1)SI - 2)NO >>"))
    except Exception as ex:
        print("Error: ", str(ex))
if bucle == 2:
 num = 0
 for precio in precios:
    if precio > num:
        num = precio
print(f"Numero mayor >> {num}")

for precio in precios:
    if precio < num:
        num = precio
     
print(f"Numero menor >>{num}")
