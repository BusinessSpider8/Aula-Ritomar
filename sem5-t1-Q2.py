#Quantidae de números pares e impares
par = 0
impar = 0
for b in range(1, 101):
    a = int(input("Digite qualquer numero: "))
    if a % 2 == 0:
        a = par
        par = par + 1
    else:
        a % 2 != 0
        a = impar
        impar = impar + 1
print(f'a quantidade de numeros pares é {par} e de impares é {impar}')
