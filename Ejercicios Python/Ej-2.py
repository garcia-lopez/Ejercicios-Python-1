#2. Dado el primer nombre, segundo nombre, primer apellido y el segundo apellido de un
#estudiante de manera individual, escriba un código en Python que permita crear un correo
#electrónico utilizando la siguiente sintaxis: primer nombre + punto (.) + primer apellido +
#“@est.uca.edu.ni”
import os
clear = lambda: os.system('cls')
clear()

print("Crear correo electronico")

print("-"*50)

primernom = str(input("Primer nombre: "))
segundonom = str(input("Segundo nombre: "))
primerapel = str(input("Primer apellido: "))
segundoapel = str(input("Segundo apellido: "))

clear()

print("-"*50)

print("Datos almacenados correctamente")

print("-"*50)

print(f"{primernom.upper()} {segundonom.upper()} {primerapel.upper()} {segundoapel.upper()} esta es su nueva direccion de correo electronico")


print(f">> {primernom.lower()}.{primerapel.lower()}@est.uca.edu.ni <<")