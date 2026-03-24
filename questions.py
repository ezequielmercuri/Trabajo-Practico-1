import random

categorias = {
    "programacion":["python","programa","variable","bucle","funcion"], 
    "tipo de datos":["cadena","entero","lista"]
}
print ("Categorias a elegir:")
for categoria in categorias:
    print(categoria)
    print()
eleccion_usuario= input("Elegi una categoria: ")
    
while eleccion_usuario not in categorias:
    print ("no se encuentra esa categoria")
    eleccion_usuario= input("Elegi una categoria")
    
palabras_no_repetidas= random.sample(
    categorias[eleccion_usuario], len(categorias[eleccion_usuario])
)

puntaje = 0
print("¡Bienvenido al Ahorcado!")
print()

for word in palabras_no_repetidas:
    guessed = []
    attempts=6
    
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
            print("¡Ganaste!")
            puntaje +=6
            print (f"terminaste con un puntaje de: {puntaje}")
            break

        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")

        letter = input("Ingresá una letra: ")
        if len(letter) !=1 or not letter.isalpha():
            print("ENTRADA NO VALIDA")
            print()
            continue 
    
        if letter in guessed:   
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            puntaje -= 1
            print("Esa letra no está en la palabra.") 

        print()

    else:
        puntaje = 0
        print(f"¡Perdiste! La palabra era: {word}")
        print(f"terminaste con un puntaje de: {puntaje}")




print("no hay mas palabras en la categoria elegida")