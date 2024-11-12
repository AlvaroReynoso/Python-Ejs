# 2.1. Escribe un programa que solicita al usuario
# que ingrese números enteros positivos y muestre
# la suma de esos números. La entrada de números
# continuará hasta que el usuario ingrese un 
# número negativo, momento en el que el programa 
# mostrará la suma total.
numeros = []

while True:
    numero = int(input("Ingresa un número entero positivo (o un número negativo para terminar): "))
    
    if numero < 0:
        break  # Salir 
    
    numeros.append(numero) #numero.append : agrega numero al array ej: 2,5,7,5,3 (en pos: 0,1,2,3,4)
suma_total = sum(numeros)
print("La suma total de los números ingresados es:", suma_total)