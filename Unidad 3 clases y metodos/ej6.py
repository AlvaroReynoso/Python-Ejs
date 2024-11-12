#6) Realizar un programa que conste de una clase llamada Alumno que tenga
# como atributos el nombre y la nota del alumno. Definir los métodos para
# inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la
# nota y si ha aprobado o no.´

class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def __str__(self):
        return(f"Nombre: {self.nombre}, Nota: {self.nota}")   #cuando pongo __str__ me permite imprimir el objeto directamente sin tener que llamar a un método y lo llamo con print(alumno1)
    
    def resultado(self):
        if self.nota>=6:
            print(f"{self.nombre} Aprobado con {self.nota}")
        else:
            print(f"{self.nombre} Reprobado con {self.nota}") #si es return abajo lo llamo con print(alumno1.resultado()) y si es print lo llamo como alumno1.resultado()

# Programa principal
alumno1 = Alumno("Ana", 8)
alumno2 = Alumno("Luis", 4)

# Imprimir información de los alumnos
print(alumno1)
print(alumno2)

alumno1.resultado()
alumno2.resultado()