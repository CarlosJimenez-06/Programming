'''11.1. Nivel de dificultad: Fácil
- Desarrolla un programa que declare una tupla con nombres de frutas y permite al usuario buscar si una fruta específica se encuentra en la tupla.'''

frutas = ("Manzana", "Pera", "Uva", "Naranja", "Mandarina", "Banano")
fruta = input("Ingrese una fruta en singular y mayuscula para buscar:\t")

if fruta in frutas:
    print(f"La fruta {fruta}, se encuentra en la tupla:\n{frutas}")
else:
    print(f"La fruta {fruta}, no se encuentra en la tupla:\n{frutas}")
