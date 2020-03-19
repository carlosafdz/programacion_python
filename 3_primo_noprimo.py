

def is_prime(numero):
    if numero < 2:
        return False
    elif numero == 0:
        return False
    elif numero == 2:
        return True
    elif numero > 2  and numero%2 == 0:
        return False
    else:
        for i in range(3,numero):
            if numero % i == 0:
                return False
                
    return True

def pruebas():
    for i in range(100):
        print(f'el {i} es {is_prime(i)}')


def main():
    numero = int(input("Numero a evaluar: "))
    result = is_prime(numero)
    if result == True:
        print(f'{numero} es primo')
    else:
        print(f'{numero} no es primo')
    

if __name__ == "__main__":
    #main()
    pruebas()