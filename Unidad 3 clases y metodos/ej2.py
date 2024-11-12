# 2- Agregarle a la clase anterior un constructor que reciba nombre y edad.
class Persona():
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

# Creación de dos objetos del tipo Persona utilizando el nuevo constructor
persona1 = Persona("Juan", 30)
persona2 = Persona("María", 25)

# Imprimir las personas por consola
persona1.print_persona()
persona2.print_persona()