'''3.1. Nivel de dificultad: Fácil
- Crea un programa que calcule el promedio de tres números ingresados por el usuario y muestre el resultado.'''

numeros = []
for i in range (1,4):
    num = float(input(f"Ingrese un numero ({i}): "))
    numeros.append(num)
sum = sum(numeros)
cantidad = len(numeros)
promedio = sum / cantidad
print(f"El promedio de los numeros proporcionados es: {promedio:.2f}")