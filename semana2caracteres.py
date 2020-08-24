def caracteres(n):
    return len(n)
def main():
    #entrada de dados
    P = input('Digite algo: ')
    #processamento
    total = caracteres(P)
    #saída de dados
    print(f'O número de caracteres da palavra {P} é: {total}.')
if __name__ == '__main__':
    main()
