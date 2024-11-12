# 10- Escribir un programa que escriba en pantalla los divisores de un número dado
num1=int(input("Ingrese numero que desee: "))
for i in range(1,num1+1,1):
    if(num1%i==0):
        print("Es divisible por",i)