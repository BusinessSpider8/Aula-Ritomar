
#valores
h = float(input('Digite a altura em metros: '))
c = float(input('Digite o comprimento em metros: '))
l = float(input('Digite a largura em metros: '))
#cálculos
A = l*c
P = 2*(h*l)+2*(h*c)
V = l*c*h
#saída
print(f'A área do piso é:{A:.2f}M^2')
print(f'A área das paredes é:{P:.2f}M^2')
print(f'O volume da sala:{V:.2f}M^3')
