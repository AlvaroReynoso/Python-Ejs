# 3-Agregarle a la clase anterior un método “es_mayor_de_edad” que devuelva
# True o False.
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_edad(self, edad):
        self.edad = edad

    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    def print_persona(self):
        print(f"Nombre: {self.get_nombre()}, Edad: {self.get_edad()}")

    def es_mayor_de_edad(self):
        return self.edad >= 18

# Creación de dos objetos del tipo Persona
persona1 = Persona("Juan", 30)
persona2 = Persona("María", 16)

# Imprimir las personas por consola
persona1.print_persona()
persona2.print_persona()

# Verificar si son mayores de edad
print(f"{persona1.get_nombre()} es mayor de edad: {persona1.es_mayor_de_edad()}")
print(f"{persona2.get_nombre()} es mayor de edad: {persona2.es_mayor_de_edad()}")
