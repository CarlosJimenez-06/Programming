'''11.2. Nivel de dificultad: Moderado
- Crea un programa que tome dos tuplas, una con nombres de estudiantes y otra con sus calificaciones, y muestre los nombres de los estudiantes que obtuvieron calificaciones por encima de un valor especificado.'''

nombres = ("Carlos", "Arvin", "Lisanyis", "Angely")
notas = (4.9, 4.7, 4.8, 4.7)

for i in range(0, len(notas)):
    print(f"El alumno(a) {nombres[i]} su calificacion es de: {notas[i]}")