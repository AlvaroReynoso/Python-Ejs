# 14) Haz un programa que escriba una pirámide inversa de los números del 1 al 
# número que indique el usuario de la siguiente forma (suponiendo que indica 6): 
# 666666 
# 55555 
# 4444 
# 333 
# 22 
# 1
num=int(input("Ingrese un numero maximo para la piramide: "))
for i in range(num,0,-1):
    for j in range(0,i,1):   
        print(i,end="")
    print()

      
    