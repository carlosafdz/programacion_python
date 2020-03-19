

PAISES = {
    "mexico":"123123",
    "colombia":"1231551",
    "españa":"989438",
    "ecuador":"21312313"
}

def main():
    
    while True:

        pais = input("Que pais quieres buscar su poblacion: ").lower()
        if pais == '':
            break
        try:
            print(f'La poblacion de {pais} es de{PAISES[pais]}')
        except KeyError:
            print("Ese pais no se encuentra en nuestros datos")
        
    

if __name__ == "__main__":
    main()