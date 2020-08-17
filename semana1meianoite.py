def Segundos(P):
    return P
def main():
    h = int(input('Digite as horas: '))
    m = int(input('Digite os minutos: '))
    s = int(input('Digite os segundos: '))
    P = (h*3600)+(m*60)+s
    print(f'A quantidade de segundos que passaram após a meia noite é: {P}')
if __name__ == '__main__':
    main()
