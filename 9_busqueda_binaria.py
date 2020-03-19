import random

def crear_lista():
    lista = list()
    for i in range (random.randint(0,20)):
        lista.append(random.randint(0,100))
    lista.sort()
    return lista

def busqueda_binaria(lista,valor,low,high):
    if low > high:
        return False
    mid = (low + high)// 2
    if lista[mid] == valor:
        return True
    elif lista[mid] > valor:
        return busqueda_binaria(lista,valor,low , mid - 1)
    else:
        return busqueda_binaria(lista, valor,mid + 1, high)
    
def main():
    lista = crear_lista()
    print(lista)
    valor = int(input("numero a buscar: "))
    resultado = busqueda_binaria(lista,valor, 0, len(lista)-1)
    if resultado == True:
        print("Si esta el numero")
    else: 
        print("No está el numero")


if __name__ == "__main__":
    main()