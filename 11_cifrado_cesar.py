import random

secreto = {}

def crear_diccionario():
    letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    letras_llave = random.sample(letras,len(letras))
    for i in range(len(letras)):
        secreto[letras[i]] = letras_llave[i]
    return secreto

def cifrado(mensaje):
    palabras = mensaje.split(' ')
    mensaje_cifrado = []
    for palabra in palabras:
        palabra_cifrada = ''
        for letra in palabra:
            palabra_cifrada += secreto[letra]

        mensaje_cifrado.append(palabra_cifrada)
    return ' '.join(mensaje_cifrado)

def descifrado(mensaje):
    palabras = mensaje.split(' ')
    mensaje_descifrado = []
    for palabra in palabras:
        palabra_descifrada = ''
        for letra in palabra:
            for key,value in secreto.items():
                if value == letra:                
                    palabra_descifrada += key

        mensaje_descifrado.append(palabra_descifrada)
    return ' '.join(mensaje_descifrado)

def main():
    crear_diccionario()
    while True:
        print("""1. cifrar un mensaje \n2. descifrar un mensaje \n3. cambiar el secreto \n4. salir """)
        accion = input("Selecciona una opcion:")
        if accion == "1":
            mensaje = input("introduce un mensaje: ")
            mensaje_cifrado = (cifrado(mensaje))
            print(mensaje_cifrado)
    
        elif accion == "2":
            mensaje = input("introduce un mensaje cifrado: ")
            mensaje_descifrado = descifrado(mensaje)
            print(mensaje_descifrado)

        elif accion == "3":
            crear_diccionario()
            print(secreto)

        else:
            break    

if __name__ == "__main__":
    main()