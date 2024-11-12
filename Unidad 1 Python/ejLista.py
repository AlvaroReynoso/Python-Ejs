frutas=["pera","manzana","naranja","banana"]
#          0       1         2         3
frutas.append("uva") #agrega un elemento al final de la lista
frutas.insert(1,"durazno") #agrega un elemento en la posicion 1
frutas.remove("banana") #elimina un elemento de la lista
frutas.pop() #elimina el ultimo elemento de la lista
print(frutas[0:3]) #imprime los elementos de la posicion 0 a la 2
print(frutas[-2]) #imprime el penultimo elemento de la lista

for fruta in frutas:
    print(fruta)    #imprime cada elemento de la lista
    
for i in range(len(fruta)):
    print(frutas[i]) #imprime cada elemento de la lista
    