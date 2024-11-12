# 2) Desarrollar una función que reciba tres números enteros positivos y verifique si 
# corresponden a una fecha válida (día, mes, año). Devolver True o False según 
# la fecha sea correcta o no.

def fechaValida(dia,mes,año):
    if(dia>0 and dia<32):
        if(mes>0 and mes<13):
            if(año>1499 and año<2025):
             return True
    else:
        return False

dia=int(input("Ingrese el dia deseado: "))
mes=int(input("Ingrese el mes deseado: "))
año=int(input("Ingrese el año deseado: "))

validado=fechaValida(dia,mes,año)
if(validado==True):
    print(f"La fecha es {validado} y es: {dia}/{mes}/{año}")
else:
    print("La fecha no es correcta")

