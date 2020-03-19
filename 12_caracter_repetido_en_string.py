"""
aababbababaabbbababaabac
asadasgasdarqweqhfdasd
qwerttyuiopasdfghjklzx
asdsadc

"""

def primer_caracter_no_repetido(secuencia):
    palabras_vistas = {}
    for idx,letter in enumerate(secuencia):
        if letter not in palabras_vistas:
            palabras_vistas[letter] = (idx,1)
        else:
            palabras_vistas[letter] = (palabras_vistas[letter][0], palabras_vistas[letter][1]+1)
    
    final_letter = []
    for key,value in palabras_vistas.items():
        if value[1] == 1:
            final_letter.append((key,value[0]))
    
    not_repeated_values = sorted(final_letter,key=lambda value: value[1])
    if not_repeated_values:
        return not_repeated_values[0][0]
    else:
        return '_'
    
def main():
    secuencia = input("Escribe una secuencia de caracteres: ")
    resultado = primer_caracter_no_repetido(secuencia)
    print(resultado)
    if resultado == '_':
        print("Todos los caracteres se repiten")
    else: 
        print(f'El caracter {resultado} es el primero que no se repite')


if __name__ == "__main__":
    main()