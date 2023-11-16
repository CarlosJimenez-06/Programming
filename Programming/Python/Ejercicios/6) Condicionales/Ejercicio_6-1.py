'''6.1. Nivel de dificultad: Fácil
- Escribe un programa que pida al usuario ingresar un número e indique si es positivo, negativo o cero.'''

num = int(input("Ingrese un numero\t"))
if num > 0:
    print(f"El numero {num}, es positivo")
elif num < 0:
    print(f"El numero {num}, es negativo")
else:
    print("El numero es cero")