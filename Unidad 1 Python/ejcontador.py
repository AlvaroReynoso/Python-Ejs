 #Ingresar 5 valores por teclado, obtener su suma y su promedio
contador=1
x=0
while contador<=5:
    suma=int(input("Ingrese numero que desee: "))
    contador=contador+1
    x+=suma
print(f"Su suma total de sus numeros es: {x}")
print(f"Su promedio es: {x/5}")
