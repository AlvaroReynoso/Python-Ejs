# Ejercicio 5: Obtener los números divibles por 7 usando una función anónima
import random
def divisiblePor7(num):
    return num%7 == 0

def generateRandomNumbers(n):
    return [random.randint(1,100) for i in range(n)]


n = int(input("Ingrese la cantidad de numeros aleatorios a generar: "))
numbers = generateRandomNumbers(n)
print(f"Los numeros generados son: {numbers}")
divisibleNumbers = [num for num in numbers if divisiblePor7(num)]
print(f"Los numeros divisibles por 7 son: {divisibleNumbers}")
