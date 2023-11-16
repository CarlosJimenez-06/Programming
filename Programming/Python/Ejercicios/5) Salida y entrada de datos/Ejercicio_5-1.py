'''5.1. Nivel de dificultad: Fácil
- Haz un programa que solicite al usuario su nombre y su edad, y luego imprima un mensaje personalizado que incluya esta información.'''

def Recibir(data):
     return input(f"Ingrese su {data}:\t")

nombre = Recibir("Nombre")
edad = Recibir("Edad")
print(f"Saludos {nombre}, felices {edad} años.")