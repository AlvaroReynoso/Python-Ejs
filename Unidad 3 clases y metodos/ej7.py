# 7- Desarrollar un programa que cargue los datos de un triángulo. Implementar una
# clase con los métodos para inicializar los atributos, imprimir el valor del lado
# con un tamaño mayor y el tipo de triángulo que es (equilátero, isósceles o
# escaleno).
class Triangulo:
    def _init_(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def imprimir_lado_mayor(self):
        lado_mayor = max(self.lado1, self.lado2, self.lado3)
        print(f"El lado mayor del triángulo es: {lado_mayor}")

    def tipo_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            print("El triángulo es equilátero.")
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            print("El triángulo es isósceles.")
        else:
            print("El triángulo es escaleno.")

# Programa principal
lado1 = float(input("Ingrese el primer lado del triángulo: "))
lado2 = float(input("Ingrese el segundo lado del triángulo: "))
lado3 = float(input("Ingrese el tercer lado del triángulo: "))

triangulo = Triangulo(lado1, lado2, lado3)

# Imprimir el lado mayor y el tipo de triángulo
triangulo.imprimir_lado_mayor()
triangulo.tipo_triangulo()