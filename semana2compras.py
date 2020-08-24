def vista(A):
    return A * 0.91
def Cvezes(A):
    return A/5
def Dvezes(A):
    return (A*1.17)/10
def main():
    #Entrada de dados
    C = float(input('Digite o valor da compra: '))
    #Processamento
    CA = vista(C)
    C5 = Cvezes(C)
    C10 = Dvezes(C)
    #Saída de dados
    print(f'O valor à vista é de:{CA:.2f}.')
    print(f'O valor em 5 vezes é de:{C5:.2f}.')
    print(f'O valor em 10 vezes é de:{C10:.2f}.')
if __name__ == '__main__':
    main()
