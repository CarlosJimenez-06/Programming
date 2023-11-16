'''3.2. Nivel de dificultad: Moderado
- Desarrolla un programa que calcule el factorial de un número ingresado por el usuario. El factorial de un número entero positivo "n" se calcula multiplicando todos los enteros positivos desde 1 hasta "n".'''

def Factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial

num = int(input("Ingrese un numero entero:\t"))
factorialNum = Factorial(num)
print(f"El factorial de {num} es igual a {factorialNum}")