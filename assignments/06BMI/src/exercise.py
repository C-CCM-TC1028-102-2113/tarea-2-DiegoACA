def main():
    #escribe tu código abajo de esta línea

    p = float(input('Peso en kg: '))
    a = float(input('Altura en m: '))

    bmi = p / a**2

    if p <= 0 or a <= 0:
        print('Revisa tus datos, alguno de ellos es erróneo.')

    else:
        if bmi < 20:
            print('PESO BAJO')
        elif 20 <= bmi < 25:
            print('NORMAL')
        elif 25 <= bmi < 30:
            print('SOBREPESO')
        elif 30 <= bmi < 40:
            print('OBESIDAD')
        elif bmi >= 40:
            print('OBESIDAD MORBIDA')

    pass
if __name__=='__main__':
    main()