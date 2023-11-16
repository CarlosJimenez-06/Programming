'''7.2. Nivel de dificultad: Moderado
- Escribe un programa que use un bucle while para calcular la suma de todos los números enteros desde 1 hasta un número ingresado por el usuario.'''
num = int(input("Ingrese un numero entero positivo:\t"))
sum = 0
index = 1
while index <= num:
    sum += index
    index += 1
print(f"La suma desde 1 hasta {num} es {sum}")