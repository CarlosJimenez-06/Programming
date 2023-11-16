'''1.2. Nivel de dificultad: Moderado
- Crea un programa que calcule el área de un triángulo. Pide al usuario que ingrese la base y la altura, y luego muestra el área.'''

base = float(input("Ingrese el valor de la base del triangulo:\t"))
altura = float(input("Ingrese el valor de la altura del triangulo:\t"))
area = (base * altura) / 2
print(f"El area de un triangulo de base {base} y altura {altura} es igual a: {area:.2f}")