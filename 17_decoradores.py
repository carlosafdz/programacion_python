

def funcion_protectora(func):
    def wrapper(password):
        if password=="contraseña":
            return func()
        else:
            print("La contraseña es incorrecta")
            
    return wrapper

@funcion_protectora
def protected_func():
    print("Tu contraseña esta segura")

if __name__ == "__main__":
    password = input("introducir contraseña: ")

    protected_func(password)

    """ el metodo sin el decorado '@decorador' seria:
    wrapper = funcion_protectora(protected_func)
    wrapper(password)
    """