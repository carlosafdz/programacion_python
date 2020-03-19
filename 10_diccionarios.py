

if __name__ == "__main__":
    diccionario = {}
    diccionario['mate'] = 9
    diccionario['fisica'] = 10
    diccionario['web'] = 8
    diccionario['base de datos'] = 9

    for key in diccionario:
        print(key)

    for value in diccionario.values():
        print(value)

    for key,value in diccionario.items():
        print(f'{key} es {value}')

    suma_calificaciones = 0
    for value in diccionario.values():
        suma_calificaciones+=value
    
    promedio = suma_calificaciones/len(diccionario.values())
    print (f'promedio es de: {promedio}')