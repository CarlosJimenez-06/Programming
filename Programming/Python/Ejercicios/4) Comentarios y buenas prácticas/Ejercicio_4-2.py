'''4.2. Nivel de dificultad: Moderado
- Crea un programa que determine si un número ingresado por el usuario es primo. Agrega comentarios que expliquen la lógica detrás de la verificación de números primos.
'''

#Crea una lista de los primeros 500 numeros primos
primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]

#Crea una funcion para verificar si el numero ingresado es primo
def esPrimo(num):
    if num in primos:
        print(f"El numero {num}, es primo")
    else:
        print(f"El numero {num}, no es primo")
#pide un numero entre 2 y 500 al usuario y luego llama a la funcion "esPrimo()"
num = int(input("Ingrese un numero entero entre 2 y 500:\t"))
esPrimo(num)