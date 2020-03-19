import random


def main():
    minimo = 1
    maximo = 100
    random_found = False
    random_number = random.randint(minimo,maximo)

    while random_found == False:
        valor = int(input(f'elige un numero del {minimo} al {maximo}:'))
        if valor > random_number:
            print("es menor")
        elif valor < random_number:
            print("es mayor")
        else:
            print("correcto")
            random_found = True

if __name__ == "__main__":
    main()