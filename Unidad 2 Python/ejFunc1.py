# 1- Desarrollar una función que reciba tres números positivos y devuelva el mayor 
# de los tres, sólo si éste es único (mayor estricto). En caso de no existir el mayor 
# estricto devolver -1. No utilizar operadores lógicos (and, or, not). Desarrollar 
# también un programa para ingresar los tres valores, invocar a la función y 
# mostrar el máximo hallado, o un mensaje informativo si éste no existe. 

def mayorEstricto(a,b,c):
    if(a>b):
        if(a>c):
            return a
        else:
            return -1
    else:
        if(b>c):
            return b
        else:
            return -1

a=int(input("Ingrese numero 1: "))
b=int(input("Ingrese numero 2: "))
c=int(input("Ingrese numero 3: "))
mayor = mayorEstricto(a,b,c)
if(mayor == -1):
    print("No existe un mayor estricto")
else:
    print(f"El mayor estricto es: {mayor}")

