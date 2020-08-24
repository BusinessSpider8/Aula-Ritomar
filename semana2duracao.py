#Entrada de dados
s = int(input('Digite a duração do evento em segundos: '))
#Processamento
H = s//3600
ss = s%3600
M = ss//60
S = ss%60
#Saída de dados
print(f'A duração do evento em segundos foi de: {H}:{M}:{S}.')

