import random

def promedio_temperaturas(temperaturas):
    suma_temperaturas = 0

    for temp in temperaturas:
        suma_temperaturas += temp
    return suma_temperaturas/len(temperaturas)

def main():
    print(temperaturas)
    print(f'promedio de la temperatura es: {promedio_temperaturas(temperaturas)}')

if __name__ == "__main__":
    temperaturas = list()
    for i in range(0,20):
        valor_random = random.randint(22,35)
        temperaturas.append(valor_random)
    main()

"""
lista.append(valor) agrega elementos al final de la lista
lista.insert(posicion,valor) agrega elementos en la posicion dada recorriendo a la derecha los demas
lista.extend(lista) (agrega los elementos de una lista a tu lista)
lista.pop(valor(opciona))  elimina el ultimo valor de la lista
lista.remove(valor) elimina el valor en la primera posicion encontrada de izquieda a derecha
lista.count(valor) cuenta la cantidad de elementos del mismo valor econtrado
lista.reverse() cambia el orden de la lista al reves
lista.sort() ordena en tamaña los elementos de la lista
del lista[posicion] elimina el elemento de la pisicion 

lista = list(string) convierte un string en una lista separando por comas cada caracter
string = ''.join(lista) convierte en string una lista de caracteres chars o strings (no valores numericos)
string.upper()
strong.lower()
string.find('valor')

"""




