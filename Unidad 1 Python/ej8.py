# 8- Escribe un programa que pida un número y nos diga si es divisible por 2, 3, 5 o 
# 7 (sólo hay que comprobar si lo es por uno de los cuatro) 

num1=float(input("Ingrese numero: "))
if(num1%7==0):
    print("El numero es divisiible por 7")
elif(num1%5==0):
    print("El numero es divisiible por 5")
elif(num1%3==0):
    print("El numero es divisiible por 3")
elif(num1%2==0):
    print("El numero es divisiible por 2")
else:
    print("El numero no es divisiible por 2, 3, 5 o 7")
    