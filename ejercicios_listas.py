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





