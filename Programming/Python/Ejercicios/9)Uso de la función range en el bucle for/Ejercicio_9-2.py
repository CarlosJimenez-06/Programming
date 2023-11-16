'''9.2. Nivel de dificultad: Moderado
- Desarrolla un programa que use un bucle for y la función range para calcular la suma de todos los números impares entre 1 y un número ingresado por el usuario.'''

num = int(input("Ingrese un numero entero positivo:\t"))
suma = 0
for i in range(1, num + 1):
    suma += i
print(f"la suma de los numeros desde 1 hasta {num} es igual a {suma}")