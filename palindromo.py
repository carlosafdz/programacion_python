def palindromo(palabra):
    reversed_letters = []
    for letra in palabra:
        reversed_letters.insert(0,letra)
    reversed_word = ''.join(reversed_letters)
    if reversed_word == palabra:
        return True
    return False

def palindromo_v2(palabra):
    reversed_word =palabra[::-1]
    if reversed_word == palabra:
        return True
    return False

def main():
    result = palindromo_v2(palabra)
    if result == True:
        print(f'{palabra} Si es un palindromo')
    else:
        print(f'{palabra} No es un palindromo')

if __name__ == "__main__":
    palabra = input("Escribe una palabra: ")
    main()