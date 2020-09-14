#Escreva um programa que leia um conjunto de 100 números inteiros positivos e determine o maiordeles.
def maior():
    n_maior = 0

    for L in range(0, 100):
        N = int(input("Digite um numero: "))
        if N > n_maior:
            n_maior = N
    return n_maior

#Saída
def main():
    M = maior()
    print(f'O maior numero desse conjuto é o:{M}')

if __name__ == '__main__':
    main()
