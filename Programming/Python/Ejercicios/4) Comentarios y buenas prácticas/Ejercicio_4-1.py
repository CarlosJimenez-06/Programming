'''4.1. Nivel de dificultad: Fácil
- Escribe un programa que imprima una serie de números del 1 al 10 en orden ascendente y luego en orden descendente. Añade comentarios que expliquen el propósito de cada parte del código.'''

numeros = list(range(1,11)) #Crea una lista de numeros desde el 1 hasta el 10

def Imprimir(lista): #Funcion para iterar e imprimir los elementos de la lista
    for i in lista: #Itera en la lista
        print(i) #Imprime el elemento iterado

Imprimir(numeros) #Imprime la lista
numeros.reverse() #Invierte el orden de la lista
Imprimir(numeros) #Imprime la lista invertida