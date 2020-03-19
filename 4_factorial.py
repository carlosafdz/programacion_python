

def factorial(numero):
    if numero == 0:
        return 1
    if numero == 1:
        return 1
    resultado = numero * factorial(numero-1)
    return resultado

def pruebas():
    for i in range(10):
        print(f'el factorial de {i} es {factorial(i)}')


def main():
    valor = int(input("selecciona un valor"))
    print(f'el factorial de {valor} es {factorial(valor)}')


if __name__ == "__main__":
    main()
    pruebas()