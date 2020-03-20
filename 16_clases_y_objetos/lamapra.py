
class Lampara():
    _LAMPS = ['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']

    def __init__(self,_is_on):
        self._is_on = _is_on
    
    def turn_on(self):
        self._is_on=True
        self._display_lamp()

    def turn_off(self):
        self._is_on =False
        self._display_lamp()

    def _display_lamp(self):
        if self._is_on == True:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])

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