'''1.3. Nivel de dificultad: Moderado
- Escribe un programa que convierta grados Celsius a grados Fahrenheit. Pide al usuario que ingrese la temperatura en grados Celsius y muestra la temperatura equivalente en grados Fahrenheit.'''

celsius = float(input("Ingrese la temperatura en grados Celsius:\t"))
fahrenheit = celsius * 1.8 + 32
print(f"La temperatura de {celsius}°C equivalen a {fahrenheit:.2f}°F")