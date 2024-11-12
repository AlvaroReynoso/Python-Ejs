# 9- Realizar una clase que administre una agenda. Se debe almacenar para cada
# contacto el nombre, el teléfono y el email. Además deberá mostrar un menú
# con las siguientes opciones: Añadir contacto, Listar contactos, Buscar contacto,
# Editar contacto, Cerrar agenda.

class Agenda:
    def __init__(self):
        self.contacto = []

    def agregarContacto(self,nombre,telefono,email):
        nombre=input("Ingrese su nombre: ")
        telefono=input("Ingrese su telefono: ")
        email=input("Ingrese su email: ")
      
persona1=Agenda.agregarContacto()
print(persona1)