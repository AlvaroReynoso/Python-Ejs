# Ejercicio 23: Comprobar si un carácter dado es una vocal.
def esVocal(char):
    vocales = "aeiou"
    return char in vocales

char = input("Ingrese un caracter: ")
if(esVocal(char)):
        print(f"El caracter {char} es una vocal")
else:
    print(f"El caracter {char} no es una vocal")
    
    
