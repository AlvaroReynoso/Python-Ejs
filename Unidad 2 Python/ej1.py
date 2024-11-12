# Función que recibe dos números y devuelve el mayor, o un mensaje si son iguales
def funcionMax(a,b):
    if(a>b):
        print(f"Su numero {a} es mayor que {b}")
    elif(b>a):
        print(f"Su numero {b} es mayor que {a}")
    else:
        raise Exception("Los numeros son iguales")      
a=int(input("Ingrese numero 1: "))
b=int(input("Ingrese numero 2: "))
funcionMax(a,b)