# 6-Escribe un programa que pida 3 números y escriba en la pantalla el mayor de 
# los tres.

n1=float(input("Ingrese numero 1: "))
n2=float(input("Ingrese numero 2: "))
n3=float(input("Ingrese numero 3: "))
if (n1>n2 and n1>n3):
    print(f"El numero {int(n1)} es mayor que {int(n2)} y que {int(n3)} ")
elif(n2>n1 and n2>n3):
    print(f"El numero {int(n2)} es mayor que {int(n1)} y que  {int(n3)}") 
else:
    print(f"El numero {int(n3)} es mayor que {int(n1)} y que {int(n2)}") 

