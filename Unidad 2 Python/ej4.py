# Ejercicio 4: Generar un conjunto de números aleatorios y determinar cuáles son impares.
#
import random
def esPar(num):
    return num%2 != 0

def generarDatosRandoms(n):
    return [random.randint(1,100) for i in range(n)]   

n = int(input("Ingrese la cantidad de numeros aleatorios a generar: "))
numeros = generarDatosRandoms(n)
print(f"Los numeros generados son: {numeros}")
numImpares = [num for num in numeros if esPar(num)]
print(f"Los numeros impares son: {numImpares}")
