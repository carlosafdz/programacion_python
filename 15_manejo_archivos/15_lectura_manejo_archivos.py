def main():
    counter = 0
    with open("15_manejo_archivos/historia.txt",'r') as f:
        #print(f.readlines())

        for line in f:
            counter += line.count('Beatriz') 

    print(f'Beatriz se encuentra {counter} veces')

if __name__ == "__main__":
    main()