import random

categories = {
    "Lenguajes": ["python", "java", "html","css"],
    "Conceptos": ["variable", "funcion", "bucle"],
    "Herramientas": ["git", "vscode", "github"],
    "Estructuras": ["lista", "tupla", "diccionario"]
}

print("¡Bienvenido al Ahorcado!")
print()

print("Elegí una categoría:")
print("a) Lenguajes")
print("b) Conceptos")
print("c) Herramientas")
print("d) Estructuras")

while True:
    option = input("Opción: ").lower()
    match option:
        case "a":
            chosen = "Lenguajes"
            break
        case "b":
            chosen = "Conceptos"
            break
        case "c":
            chosen = "Herramientas"
            break
        case "d":
            chosen = "Estructuras"
            break
        case _:
            print("Opción inválida, intentá de nuevo.")

word = random.choice(categories[chosen])
print(f"\nLa categoría elegida fue {chosen}\n")

letters = set("abcdefghijklmnopqrstuvwxyz")
guessed = []
attempts = 6
score = 0

while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)

    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        score+=6
        print("¡Ganaste!")
        break

    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")

    letter = input("Ingresá una letra: ").lower()

    if len(letter) != 1 or letter not in letters:
        print("Entrada no válida")
        continue
    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        score-=1
        print("Esa letra no está en la palabra.")

    print()
else:
    score=0
    print(f"¡Perdiste! La palabra era: {word}")

print(f'Puntaje final: {score}')
