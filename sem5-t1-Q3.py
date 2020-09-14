#Ler um conjunto de 100 números inteiros e exibir o valor médio com 2 casa decimais
s = 0
for L in range(0, 100):
    #entrada de dados
    A = int(input("Digite um numero: "))
    #Processamento
    s = A + s
    media = s / 100
#Saida de dados
print(f'A media desse conjunto de 100 números é {media:.2f}')
