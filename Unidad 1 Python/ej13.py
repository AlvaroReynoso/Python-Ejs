# 13) Realiza un programa que escriba una pirámide del 1 al 30 de la siguiente 
# forma: 
# 1 
# 22 
# 333 
# 4444 
# 55555 hasta 9

for i in range(1,10,1):
    for j in range(0,i,1):
        print(i,end="")
    print("")