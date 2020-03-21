
class Contact:
    def __init__(self,nombre,telefono,email):
        self._nombre = nombre
        self._telefono = telefono
        self._email = email
    
class ContactBook:
    def __init__(self):
        self._contacts= []

    def mostar(self):
        self._contacts[0]._nombre = 'b'
        print(self._contacts[0]._nombre)


    def add(self,name,phone,email):
        print("Contacto agregado")
        contact = Contact(name,phone,email)
        self._contacts.append(contact)
        print(f'contacto agregado: nombre:{name} phone:{phone} email:{email}')

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)
            

    def _print_contact(self,contact):
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        print(f'nombre: {contact._nombre}')
        print(f'telefono: {contact._telefono}')
        print(f'email: {contact._email}')
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

    def delete(self,nombre):
        for idx,contact in enumerate(self._contacts):
            if contact._nombre.lower() == nombre.lower():
                del self._contacts[idx]
                break

    def search(self, nombre):
        for idx,contact in enumerate(self._contacts):
            if contact._nombre.lower() == nombre.lower():
                print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
                print(f'nombre: {contact._nombre}')
                print(f'telefono: {contact._telefono}')
                print(f'email: {contact._email}')
                print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
                break
        else:
            self._notFound(nombre)
    
    def _notFound(self,nombre):
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        print(f'no se encuentra registrado {nombre}')
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

    def update_menu(self,nombre):
        self.search(nombre)
        accion = input(""" 
            a. nombre
            b. telefono
            c. email
        """)
        if accion == "a":
            dato = input("introduce el nombre: ")
            self.update(nombre,dato,accion)

        elif accion == "b":
            dato = input("introduce el telefono: ")
            self.update(nombre,dato,accion)
        
        elif accion == "c":
            dato = input("introduce el email")
            self.update(nombre,dato,accion)

        else:
            print("opcion no valida") 

    def update(self,nombre,dato,opcion):
        for idx,contact in enumerate(self._contacts):
            if contact._nombre.lower() == nombre.lower():
                if opcion == "a":
                    self._contacts[idx]._nombre = dato
                
                elif opcion == "b":
                    self._contacts[idx]._telefono = dato

                elif opcion == "c":
                    self._contacts[idx]._email = dato

                print("contacto actualizado")
                break
        else:
            self._notFound(nombre)

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
        
        ''')

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
        

        pass

if __name__ == "__main__":
    run()