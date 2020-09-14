#Escreva um programa que gere a seguinte sequência: 10, 20, 30, 40, ..., 990, 1000.
for L in  range(10, 1010, 10):
    print(L, end='')
    if L == 1000:
        print('.')
    else:
        print(',', end=' ')
