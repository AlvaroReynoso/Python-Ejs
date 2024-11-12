# 11- Escribir un programa que nos diga si un número dado es primo (no es divisible 
# por ninguno otro número que no sea él mismo o la unidad)

num=int(input("Ingrese numero deseado: "))
contador=2
while (contador<num):
    if(num%contador==0):
        print(f"El numero {num} no es primo")
        break
    else:
        print(f"El numero {num} es primo")
        break        