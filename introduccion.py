print("hola mundo")
numero = 3
print("mi numero es", numero)
print(f"mi numero es {numero}")
nombre = input("Ingrese su nombre: ")
print(f"El nombre recibido adentro de la terminal es {nombre}")
#El tipo de variable: 
apellido = "Reynoso"
edad = 26
altura= 1.90
soySoltero = True
print(f"la persona {apellido}, tiene la edad {edad}, tiene una altura de {altura} y es {soySoltero}")
#tipo de operadores
numero_1 = 5
numero_2 =int("5")
#print(numero_1 + numero_2)
print(type(numero_2))
print(numero_1 + numero_2)
print(numero_1 - numero_2)
print(numero_1 * numero_2)
print(numero_1 / numero_2)
print(numero_1 // numero_2)
print(numero_1 ** numero_2)
print(numero_1 % numero_2)
print(numero_1 == numero_2)
print(numero_1 != numero_2)
print(numero_1 < numero_2)
print(numero_1 > numero_2)
print(numero_1 <= numero_2)
print(numero_1 >= numero_2)
#numero_1 += numero_2
#print(numero_1)
numero_1 -= numero_2
print(numero_1)


#escriba un programa que tome 2 cadenas de texto y las concatene
nombre="Alvaro"
apellido="Reynoso"
nombre_completo=nombre + " " + apellido
print(nombre_completo)


#LISTA (se hacen con corchetes)
colores=["azul","rojo","salmon"]
#     0      1      2   
colorObjeto= input("Ingrese color: ")
if(colorObjeto in colores):
    print("El color{colorObjeto} se encuentra en la lista")
else:
    print("No se encuentra en la lista")

#.lower() es para min .upper() para mayus


#EJERCICIOS

# 1. Escribe un programa que identifique el color
# de un objeto y muestre un mensaje según el color.



# 2. Escribe un programa que muestre
# los números del 0 al 4 usando un ciclo while.

# 2.1. Escribe un programa que solicita al usuario
# que ingrese números enteros positivos y muestre
# la suma de esos números. La entrada de números
# continuará hasta que el usuario ingrese un 
# número negativo, momento en el que el programa 
# mostrará la suma total.

# 3.Escribe un programa que muestra la primer,
# última u otra letra de una cadena de carcateres,
# inclusive una rebanada.

# 4. Crear una lista de frutas y mostrar en consola
# algunas frutas de la lista, también por rebanadas.

# 5. Escribe un programa que recorra una lista de 
# frutas y muestre cada fruta.

# 5.1 Agregar otras frutas a la lista.

# 5.2 Escribe un programa verifique si una fruta 
# específica está en una lista de frutas y muestra
# un mensaje correspondiente.

# 6. Escribe un programa que recorra una lista
# de números y muestre si cada número es par o impar.

# 7. Escribe un programa que recorra una cadena de 
# texto y cuente cuántas veces aparece la letra 'a' en la cadena.

# 8. Integrador:
# Escribe un programa que permita a un usuario crear
# una lista de nombres. El programa continuará pidiendo
# nombres hasta que el usuario ingrese "fin". Luego, 
# el programa mostrará la lista de nombres en orden alfabético,
# indicará cuántos nombres empiezan con la letra 'A' o 'E', 
# y mostrará si un nombre específico está en la lista.