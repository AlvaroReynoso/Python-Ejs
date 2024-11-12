"""Actividad Práctica - Python Unidad 3
1) Crear la clase Persona con los métodos “set_nombre”, “set_edad”,
“get_nombre”, “get_edad” y “print_persona”. Luego crear dos objetos del tipo
Persona e imprimirlos por consola.
2) Agregarle a la clase anterior un constructor que reciba nombre y edad.
3) Agregarle a la clase anterior un método “es_mayor_de_edad” que devuelva
True o False."""
class Persona:
    def _init_(self):
        self.nombre = ""
        self.edad = 0
        
    def set_nombre(self,nombre):
        self.nombre = nombre
        
    def set_edad(self, edad):
        self.edad = edad
    
    def get_nombre(self):
        return self.nombre 
        
    def get_edad(self):
        return self.edad 
    
    def print_persona(self):
        print(f"Nombre: {self.get_nombre()}, Edad: {self.get_edad()}")

# Creación de dos objetos del tipo Persona
persona1 = Persona()
persona1.set_nombre("Juan")
persona1.set_edad(30)

persona2 = Persona()
persona2.set_nombre("María")
persona2.set_edad(25)

# Imprimir las personas por consola
persona1.print_persona()
persona2.print_persona()