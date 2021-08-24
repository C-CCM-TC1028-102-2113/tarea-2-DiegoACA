
def main():
    #Escribe tu código debajo de esta línea

    e = int(input('Ingresa tu edad: '))
    i = str(input('¿Tienes identificación oficial? (s/n): '))

    if e >= 0 and (i == "s" or i == "n"):
        if e >= 18 and i == "s":
            print("Trámite de licencia concedido")
        elif e < 18:
            print("No cumples requisitos")
        elif i != "s":
            print("No cumples requisitos")
    else:
        print('Respuesta incorrecta')

    pass


if __name__ == '__main__':
    main()
