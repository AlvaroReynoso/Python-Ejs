#5) Agregarle un método estático “get_mayor” que reciba dos objetos Persona y devuelva el de edad mayor
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

    @staticmethod
    def get_mayor(persona1, persona2):
        if persona1.get_edad() > persona2.get_edad():
            return persona1
        else:
            return persona2

# Creación de dos objetos del tipo Persona
persona1 = Persona("Juan", 30)
persona2 = Persona("María", 25)

# Imprimir las personas por consola
persona1.print_persona()
persona2.print_persona()

# Comparar quién es mayor
mayor = Persona.get_mayor(persona1, persona2)
print(f"La persona mayor es: {mayor.get_nombre()} con {mayor.get_edad()} años.")