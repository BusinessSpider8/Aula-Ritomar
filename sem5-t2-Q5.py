#Escreva um programa que simula o valor (com duas casas decimais) da prestação de uma compra parcelada sem juros de 1x até 24x. O valor da compra é digitado pelo usuário. O valor da prestação sem juros, deve ser calculado como o valor da compra dividido pelo número de prestações de 1 até 24.
valor = int(input("Informe o valor da compra: "))
total = 0
for L in range(1, 25):
    total += 1
    if True:
        parcela = valor / total
        print(f'{total}x de R$ {parcela:.2f}')
