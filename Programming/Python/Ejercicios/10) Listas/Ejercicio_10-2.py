'''10.2. Nivel de dificultad: Moderado
- Escribe un programa que tome una lista de palabras como entrada y muestre la palabra más larga de la lista.'''

words = []
def longestWord(w1, w2):
    if len(w1) > len(w2):
        return w1
    elif len(w1) < len(w2):
        return w2
    else:
        return list(w1, w2)

print("Ingrese una palabra para anexar y un cero (0) para cancelar:\t")
while True:
    word = input("Ingresar:\t")
    if word == '0':
        break
    else:
        words.append(word)
longWord = ""        
for word in words:
    longWord = longestWord(longWord, word)
print(f"De la siguiente lista:\n{words}\nLa palabra(s) mas larga(s) es {longWord}")