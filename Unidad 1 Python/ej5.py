# 5- Escribe un programa que pida dos números y escriba en la pantalla cual es el 
# mayor.

n1=float(input("Ingrese numero 1: "))
n2=float(input("Ingrese numero 2: "))
if (n1>n2):
    print(f"El numero {int(n1)} es mayor que {int(n2)}")
else:
    print(f"El numero {int(n2)} es mayor que {int(n1)}")
