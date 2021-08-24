
def main():
    #Escribe tu código debajo de esta línea

    e = int(input("edad?"))
    i = str(input("identificaciòn? (s/n)"))

    if e >= 0 and (i == "s" or i == "n"):
        if e >= 18 and i == "s":
            print("Trámite de licencia concedido")
        else:
            print("No cumples requisitos")
    else:
        print("Datos invalidos")

    pass


if __name__ == '__main__':
    main()
