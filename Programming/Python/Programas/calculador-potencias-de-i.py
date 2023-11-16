#Crear un diccionario que almacene las potencias de i del 0 al 10
""" Potencias de I:
i^0 = 1, i^4 = 1, i^8 = 1
i^1 = i, i^5 = i, i^9 = i
i^2 = -1, i^6 = -1, i^10 = -1
i^3 = -i, i^7 = -i
"""
""" Eventos:
****1****
1 * 1 = 1
1 * -1 = -1
i * 1 = i
1 * -i = i
****-1****
-1 * 1 = -1
-1 * -1 = 1
-1 * i = -i
-1 * -i = i
****i****
i * i = i2 = -1
i * -1 = -i
i * 1 = i
i * -i = 1
****-1****
-i * i = -1
-i * -1 = i
-i * 1 = -i
-i * -i = 1
"""
#Crear una funcion para determinar el valor de i a una gran potencia in = i4*q *ir

potenciasI = {0:1, 1:"i", 2:-1, 3:"-i", 4:1, 5:"i", 6:-1, 7:"-i", 8:1, 9:"i", 10:-1}

def calcIvalue():
    n = int(input("\nIngrese el valor de la potencia de 'i'\n"))
    q = int(n/4)
    r = int(n%4)
    i = potenciasI[r]
    print(f"\ni^{n} = (i^4)^q * i^{r} \n= (1)^{q} * i^{r} \n= 1 * {i} \n= {i}")
    print("--------------------------------------------")

while True:    
    calcIvalue()
