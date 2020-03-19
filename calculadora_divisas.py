
usd = {
	"mxn":23.7,
    "eur":0.91
}
eur = {
    "usd":1.1,
    "mxn":25.88
}

mxn = {
    "eur":0.039,
    "usd":0.042
}

def conversion(base,cambio,cantidad):
    if cambio != "usd" or cambio != "mxn" or cambio != "eur":
        print("moneda {cambio} no aceptada")
    if base == "usd":
        respuesta = cantidad * usd[cambio]
    elif base == "eur":
        respuesta = cantidad * eur[cambio]
    elif base == "mxn":
        respuesta = cantidad * mxn[cambio]

    else: 
        print("moneda {base} no aceptada")

    return f'{cantidad} {base} a {cambio} son: {respuesta}'

def pruebas():
    print(conversion("usd","eur",1000))
    print(conversion("usd","mxn",1000))
    print(conversion("eur","usd",1000))
    print(conversion("eur","mxn",1000))
    print(conversion("mxn","usd",1000))
    print(conversion("mxn","eur",1000))

def main():
    print("###### Calculadorea de divisas ##########")
    print("Pesos Mexicanos: MXN \nDolares Americanos: USD \nEuros: EUR")
    print(" ")
    divisa_base = input("Que divisa quieres convertir: ")
    divisa_cambio = input("A que divisa la deseas convertir: ")
    cantidad = float(input("Cuanto deseas convertir: "))
    print(conversion(divisa_base,divisa_cambio,cantidad))

if __name__ == "__main__":
    pruebas()
    main()