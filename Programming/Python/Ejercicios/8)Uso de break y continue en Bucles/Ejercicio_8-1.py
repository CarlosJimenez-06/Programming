'''8.1. Nivel de dificultad: Moderado
- Implementa un programa que use un bucle for para imprimir todos los números del 1 al 20, pero omite los números que son múltiplos de 4. Utiliza la instrucción continue para lograr esto.'''

for i in range(0,21):
    if i % 4 == 0:
        continue
    else:
        print(i)