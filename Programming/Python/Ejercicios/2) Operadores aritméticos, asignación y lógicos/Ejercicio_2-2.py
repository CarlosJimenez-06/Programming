'''2.2. Nivel de dificultad: Moderado
- Escribe un programa que pida al usuario un número y luego determine si es divisible por 3 y por 5 al mismo tiempo. Muestra un mensaje que indique si es divisible o no.'''

num = int(input("ngrese un numero entero:\t"))
esDivTres = num % 3 == 0
esDivCinco = num % 5 == 0
esDivTresyCinco = esDivTres == True and esDivCinco == True
if esDivTresyCinco == True:
    print(f"El numero {num}, es divisible por 3 y 5 a la vez")
else:
    print(f"El numero {num}, no es divisible por 3 y 5 a la vez")