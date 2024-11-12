class Agenda:
    def __init__(self):
        self.contacto = []

    def agregarContacto(self):
        nombre=input("Ingrese su nombre: ")
        telefono=input("Ingrese su telefono: ")
        email=input("Ingrese su email: ")
    
        self.contacto.append([nombre,telefono,email])
    
    def listarContacto(self):
        for i in self.contacto:
            print(i)    

persona1=Agenda()            
persona1.agregarContacto()

persona1.listarContacto()