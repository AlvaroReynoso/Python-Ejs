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

