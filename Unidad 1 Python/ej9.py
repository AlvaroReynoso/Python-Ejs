#9- Añadir al ejercicio anterior que nos diga por cuál de los cuatro es divisible (hay 
# que decir todos por los que es divisible) 
numero = int(input("Introduce un número: "))
numeroDiv=False
if (numero%7==0):
    print("El numero es divisible por 7")
    numeroDiv=True
if (numero%5==0):
    print("El numero es divisible por 5")
    numeroDiv=True
if (numero%3==0):
    print("El numero es divisible por 3")
    numeroDiv=True
if (numero%2==0):
    print("El numero es divisible por 2")
    numeroDiv=True
if not numeroDiv:
    print("El numero no es divisible por 2, 3, 5 o 7")
    numeroDiv=False
    
    