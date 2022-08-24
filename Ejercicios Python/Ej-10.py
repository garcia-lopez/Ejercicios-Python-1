"""Dado el numero de cuenta, el saldo y el monto de retiro de una cuenta de ahorra verifique
si la persona puede realizar el retiro. Una vez evaluado debe mostrarse el saldo que queda
después del retiro."""
import os
clear = lambda: os.system('cls')
clear()
saldo = 100
cuenta = []
print("<<Banco>>")
num = int(input("Numero de cuenta: "))
cuenta.append(num)

clear()

credencial = int(input("Digite su numero de cuenta>> "))

for num in cuenta:
    credencial == num

print("---Menu de opciones---")
print("1- Depositar ")
print("2- Retirar")
print("3- Ver estado de cuenta")

opc = int(input("Opcion: "))

if opc == 1:
    deposito = float(input("Deposito << "))
    saldo = saldo + deposito 
    print(f"Su saldo ahora es de {saldo}")

elif opc == 2:
    retiro = float(input("Retiro >>"))
    if retiro <= saldo:
        saldo = saldo - retiro
        print(f"Saldo restante << {saldo}")
    else: 
        print(f"Saldo insuficiente >> {saldo}")

elif opc == 3:
    print(f"Saldo disponible {saldo}")

