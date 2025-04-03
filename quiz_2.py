
Total = int(input())

Cantidad = []

for N in range(Total):
    Cantidad.append(int(input()))

def Calcular(numero):
    if (numero % 2 == 0 and numero > 0):
        return "EVEN POSITIVE"
    elif (numero % 2 == 0 and numero < 0):
        return "EVEN NEGATIVE"
    elif (numero % 2 == 1 and numero > 0):
        return "ODD POSITIVE"
    elif (numero % 2 == 1 and numero < 0):
        return "ODD NEGATIVE"
    elif (numero == 0):
        return "NULL"

for NumeroUtilizado in range(len(Cantidad)):
    print(Calcular(Cantidad[NumeroUtilizado]))s