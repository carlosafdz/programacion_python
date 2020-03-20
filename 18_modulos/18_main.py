from lamp import Lampara

def main():
    lamp = Lampara(_is_on=True)

    while True:
        print(''' Que desea hacer
            p. prender 
            a. apagar
            s. salir
        ''')

        accion = input("opcion: ")
        if accion == 'p':
            lamp.turn_on()
        elif accion == 'a':
            lamp.turn_off()
        elif accion == 's':
            break
        else:
            print('opcion no valida')


if __name__ == "__main__":
    main()