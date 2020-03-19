

def main():
    with open("15_manejo_archivos/numeros.txt",'w') as f:
        for i in range(0,9):
            f.write(str(i))
    

if __name__ == "__main__":
    main()