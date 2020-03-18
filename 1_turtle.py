import turtle

def avanzar(tortuga,size):
    tortuga.forward(size)

def retroceder(tortuga,size):
    tortuga.backward(size)

def angulo(tortuga,angle):
    tortuga.left(angle)


def dibujar_tortuga(tortuga,direccion="0",size=0,angle=0):
    

    if direccion == "1":
        avanzar(tortuga,size)
    
    elif direccion == "2":
        retroceder(tortuga,size)

    elif direccion == "0":
        print(type(angle))
        angulo(tortuga,angle)        


def main():
    x = 0
    angle = 0
    direccion = 0
    size = 0
    window = turtle.Screen()
    david = turtle.Turtle()
    while(x < 5):    
        print("1: distancia \n 2: direccion")
        accion = input("Que hará la tortuga: ")
        if accion == "1":
            direccion = input("1.adelante o 2.atras")
            size = int(input("cuanto avanzará: "))
        
        elif accion == "2":
            direccion="0"
            angle = int(input("Hacia donde va a mirar: "))
        
        dibujar_tortuga(david,direccion,size,angle)
        x+=1
    turtle.mainloop()

if __name__ == "__main__":
    main()