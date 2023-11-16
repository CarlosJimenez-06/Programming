'''2.1. Nivel de dificultad: Fácil
- Crea un programa que tome un número entero como entrada y determine si es par o impar. Imprime un mensaje apropiado.'''

num = int(input("Ingrese un numero entero:\t"))
esPar = num % 2 == 0
if esPar == True:
    print(f"El numero {num}, es par.")
else:
    print(f"El numero {num}, es impar.")