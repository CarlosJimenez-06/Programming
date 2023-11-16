'''6.2. Nivel de dificultad: Moderado
- Desarrolla un programa que solicite al usuario ingresar tres números y luego determine cuál de los tres es el mayor.'''

num1 = int(input("Ingrese el primer numero:\t"))
num2 = int(input("Ingrese el segundo numero:\t"))
num3 = int(input("Ingrese el tercer numero:\t"))
if num1 > num2 and num1 > num3:
    print(f"El numero {num1}, es mayor a {num2} y {num3}")
elif num2 > num1 and num2 > num3:
    print(f"El numero {num2}, es mayor a {num1} y {num3}")
elif num3 > num1 and num3 > num2:
    print(f"El numero {num3}, es mayor a {num1} y {num2}")