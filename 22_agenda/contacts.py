from ContactBook import ContactBook
import csv

def run():    

    contact_book = ContactBook()
    
    with open("22_agenda/contactos.csv",'r') as f:
        reader = csv.reader(f)
        for idx,row in enumerate(reader):
            if idx == 0:
                continue
            else:
                contact_book.add(row[0],row[1],row[2])


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