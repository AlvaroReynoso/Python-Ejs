# 1. Escribe un programa que identifique el color
# de un objeto y muestre un mensaje según el color.
colores=["azul","rojo","salmon"]
#     0      1      2   
colorObjeto= input("Ingrese color: ")
if(colorObjeto in colores):
    print(f"El color {colorObjeto} se encuentra en la lista")
else:
    print("No se encuentra en la lista")
