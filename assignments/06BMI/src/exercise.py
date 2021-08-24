def main():
    #escribe tu código abajo de esta línea

    p = float(input("Peso?"))
    a = float(input("Altura?"))

    bmi = p / a**2

    if bmi < 20:
        print("peso bajo")
    elif 20 <= bmi < 25:
        print("normal")
    elif 25 <= bmi < 30:
        print("sobrepeso")
    elif 30 <= bmi < 40:
        print("obesidad")
    elif bmi >= 40:
        print("obesidad morbida")

    pass
if __name__=='__main__':
    main()