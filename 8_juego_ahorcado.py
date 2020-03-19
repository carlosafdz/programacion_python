import random

IMAGENES = [
    ''' 
    +=======+
    |       |
            |
            |
            |
            |
            ======
    
    ''',
    ''' 
    +=======+
    |       |
    O       |
            |
            |
            |
            ======
    
    ''',
    ''' 
    +=======+
    |       |
    O       |
    |       |
            |
            |
            ======
    
    ''',
    ''' 
    +=======+
    |       |
    O       |
   /|       |
            |
            |
            ======
    
    ''',
    ''' 
    +=======+
    |       |
    O       |
   /|\      |
            |
            |
            ======
    
    ''',
    ''' 
    +=======+
    |       |
    O       |
   /|\      |
   /        |
            |
            ======

    ''',
    ''' 
    +=======+
    |       |
    O       |
   /|\      |
   / \      |
            |
            ======


    ''',
    ''' '''
    
    ]

PALABRAS = ["lavadora","secadora","pepel","computadora"]


def palabra_random():
    idx = random.randint(0,len(PALABRAS)-1)
    return PALABRAS[idx]

def mostrar_tablero(palabra_escondida,intentos):
    print(IMAGENES[intentos])
    print('')
    print(palabra_escondida)
    print("*---**---**---**---**---**---**---**---**---**---*")

def main():
    palabra = palabra_random()
    palabra_escondida = ["_"] * len(palabra)
    intentos = 0
    
    while True:

        mostrar_tablero(palabra_escondida,intentos)
        letra = input("escoge una letra: ")

        indice_letras = []
        for i in range(len(palabra)):
            if palabra[i] == letra:
                indice_letras.append(i)
        if len(indice_letras) == 0:
            intentos = intentos + 1
            if intentos == 7:
                mostrar_tablero(palabra_escondida,intentos)
                print(f'Perdiste..... la palabra correcta era {palabra}')
                break
        else:
            for i in indice_letras:
                palabra_escondida[i] = letra
            indice_letras = []

        try:
            palabra_escondida.index("_")

        except ValueError:
            print(" ")
            print("ganaste!!!")
            break

def pruebas_tablero():
    mostrar_tablero("palabra",0)
    mostrar_tablero("palabra",1)
    mostrar_tablero("palabra",2)
    mostrar_tablero("palabra",3)
    mostrar_tablero("palabra",4)
    mostrar_tablero("palabra",5)
    mostrar_tablero("palabra",6)

if __name__ == "__main__":
    main()
    #pruebas_tablero()