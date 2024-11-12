# 4-Agregarle un método “es_mayor_que” el cual recibe un objeto persona y
# compara su edad con la del objeto actual
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

    def es_mayor_que(self, otra_persona):
        return self.edad > otra_persona.get_edad()

# Creación de dos objetos del tipo Persona
persona1 = Persona("Juan", 30)
persona2 = Persona("María", 25)

# Imprimir las personas por consola
persona1.print_persona()
persona2.print_persona()

# Comparar edades
if persona1.es_mayor_que(persona2):
    print(f"{persona1.get_nombre()} es mayor que {persona2.get_nombre()}.")
else:
    print(f"{persona1.get_nombre()} no es mayor que {persona2.get_nombre()}.")