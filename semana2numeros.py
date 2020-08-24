#entrada de dados
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
n4 = int(input('Digite o quarto número: '))
n5 = int(input('Digite o quinto número: '))
#processamento
m = (n1+n2+n3+n4+n5)/5
#saída
print(max(n1, n2, n3, n4, n5))
print(min(n1, n2, n3, n4, n5))
print(f'A média dos números é: {m}.')
