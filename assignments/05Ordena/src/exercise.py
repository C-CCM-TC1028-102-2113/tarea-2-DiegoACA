def main():
    # Escribe el código adecuado para completar el programa

    x = int(input("Ingresa el primer número: "))
    y = int(input("Ingresa el segundo número: "))
    z = int(input("Ingresa el tercer número: "))

    if x > y and x > z:
        if y > z:
            print(x,y,z,sep=", ")
        else:
            print(x,z,y,sep=", ")
    elif y > x and y > z:
        if x > z:
            print(y,x,z,sep=", ")
        else:
            print(y,z,x,sep=", ")
    elif z > y and z > x:
        if y > x:
            print(z,y,x,sep=", ")
        else:
            print(z,x,y,sep=", ")


    pass


if __name__=='__main__':
    main()
