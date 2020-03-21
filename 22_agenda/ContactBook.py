from Contact import Contact
import csv

class ContactBook:
    def __init__(self):
        self._contacts= []

    def add(self,name,phone,email):
        print("Contacto agregado")
        contact = Contact(name,phone,email)
        self._contacts.append(contact)
        self._save()
        print(f'contacto agregado: nombre:{name} phone:{phone} email:{email}')

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def delete(self,nombre):
        for idx,contact in enumerate(self._contacts):
            if contact._nombre.lower() == nombre.lower():
                del self._contacts[idx]
                self._save()
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

    def _save(self):

        with open("22_agenda/contactos.csv",'w') as f:
            writer = csv.writer(f)
            writer.writerow(('nombre', 'telefono', 'email'))

            for contact in self._contacts:
                writer.writerow((contact._nombre,contact._telefono,contact._email))
        

    def _notFound(self,nombre):
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        print(f'no se encuentra registrado {nombre}')
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

    def _print_contact(self,contact):
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        print(f'nombre: {contact._nombre}')
        print(f'telefono: {contact._telefono}')
        print(f'email: {contact._email}')
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
