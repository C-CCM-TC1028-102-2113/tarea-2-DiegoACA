def main():
    # Escribe el código adecuado para completar el programa

    x = int(input("Ingresa el primer número: "))
    y = int(input("Ingresa el segundo número: "))
    z = int(input("Ingresa el tercer número: "))

    if x != y and x != z and z != y:
        if x > y and x > z:
            if y > z:
                print(z)
                print(y)
                print(x)
            else:
                print(y)
                print(z)
                print(x)
        elif y > x and y > z:
            if x > z:
                print(z)
                print(x)
                print(y)
            else:
                print(x)
                print(z)
                print(y)
        elif z > y and z > x:
            if y > x:
                print(x)
                print(y)
                print(z)
            else:
                print(y)
                print(x)
                print(z)
    else:
        print("nùmeros no validos")

    pass


if __name__=='__main__':
    main()
