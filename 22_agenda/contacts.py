from ContactBook import ContactBook

def run():    

    contact_book = ContactBook()
    
    while True:
        comando = input('''
        Que desea hacer
        a. añadir contacto
        b. actualizar contacto
        c. buscar contacto
        d. eliminar contacto
        e. listar contacto
        f. salir    
        : ''')

        if comando == 'a':
            print("añadir contacto")
            nombre = input("Escribe el nombre de la persona: ")
            telefono = input("Escribe el telefono de la persona: ")
            email = input("ingrese el email de la persona: ")

            contact_book.add(nombre,telefono,email)

        elif comando == 'b':
            print("actualizar contacto")
            nombre = input("Escribe el nombre de la persona: ")
            contact_book.update_menu(nombre)

        elif comando == 'c':
            print("buscar contacto")
            nombre = input("Escribe el nombre de la persona: ")
            contact_book.search(nombre)

        elif comando == 'd':
            print("eliminar contacto")
            nombre = input("Escribe el nombre de la persona: ")
            contact_book.delete(nombre)

        elif comando == 'e':
            print("listar contactos")
            contact_book.show_all()

        elif comando == 'f':
            print("salir ")
            break

        else:
            print("opcion no valida")

if __name__ == "__main__":
    run()