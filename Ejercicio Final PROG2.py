# 37. Sistema de Gestión de Talleres Educativos
# ● Descripción: Gestiona los participantes de un taller educativo, calculando el costo
# total del taller por participante.
# ● Funcionalidades:
# ○ Registrar Participante: Con nombre, edad y tipo de taller.
# ○ Listar Participantes: Muestra todos los participantes registrados.
# ○ Calcular Costo Taller: Incluye el costo del taller y material.
# ● Clase Participante:
# ○ Atributos: Nombre, Edad, Taller, Material, Costo Total.
# ○ Cálculo: Costo Total = Costo del Taller + Costo del
# Material.

class Participante:
    def __init__(self, nombre, edad, taller, costo_taller, costo_material):
        self.nombre = nombre
        self.edad = edad
        self.taller = taller
        self.costo_taller = costo_taller
        self.costo_material = costo_material
        self.costo_total = self.calcular_costo_total()

    def calcular_costo_total(self):
        return self.costo_taller + self.costo_material
    ##self mismo obj que estoy
    def __str__(self):
        return (f"Nombre: {self.nombre}, Edad: {self.edad}, Taller: {self.taller}, "
                f"Costo Taller: {self.costo_taller}, Costo Material: {self.costo_material}, "
                f"Costo Total: {self.costo_total}")


class SistemaGestionTalleres:
    def __init__(self):
        self.participantes = []  # Lista para guardar los participantes

    def registrar_participante(self):
        nombre = input("Nombre del participante: ")

        # Validación para la edad
        while True:
            edad = int(input("Edad del participante: "))
            if edad <= 0:
                print("La edad no puede ser negativa. Intente de nuevo.")
            else:
                break
        
        taller = input("Tipo de taller: ")

        # Validación para el costo del taller
        while True:
            costo_taller = float(input("Costo del taller: "))
            if costo_taller <= 0:
                print("El costo del taller no puede ser negativo. Intente de nuevo.")
            else:
                break
        
        # Validación para el costo del material
        while True:
            costo_material = float(input("Costo del material: "))
            if costo_material <= 0:
                print("El costo del material no puede ser negativo. Intente de nuevo.")
            else:
                break

        participante = Participante(nombre, edad, taller, costo_taller, costo_material)
        
        # Agrego el participante a la lista
        self.participantes.append(participante)
        print("Participante registrado exitosamente.")

    # Muestra los participantes registrados
    def listar_participantes(self):
        if not self.participantes:
            print("No hay participantes registrados.")
        else:
            for participante in self.participantes:
                print(participante)
                
    # Calculo el costo total del taller por participante
    def calcular_costo_taller(self):
        for participante in self.participantes:
            print(f"{participante.nombre}: Costo Total = {participante.costo_total}")
            
    # Menú de opciones 
    def menu(self):
        while True:
            print("\n--- Sistema de Gestión de Talleres Educativos ---")
            print("1. Registrar Participante")
            print("2. Listar Participantes")
            print("3. Calcular Costo Taller")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.registrar_participante()
            elif opcion == '2':
                self.listar_participantes()
            elif opcion == '3':
                self.calcular_costo_taller()
            elif opcion == '4':
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")

# Inicializo o arranco el sistema
if __name__ == "__main__":
    sistema = SistemaGestionTalleres()
    sistema.menu()
