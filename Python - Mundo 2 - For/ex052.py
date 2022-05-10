print('=~=~=~=~=~=~='*7)
print('NÚMEROS PRIMOS')
print('=~=~=~=~=~=~='*7)

num = int(input("Digite um número: "))

while num <= 0:
    print('\033[34mValor inválido, tente novamente.\033[m')
    num = int(input("Digite um número: "))
cont = 0
for i in range(1, num + 1):
        
    if num % i == 0:
        cont += 1
        print('\033[33m', end='')
    else:
        print('\033[34m', end='')
    print('{} '.format(i), end='')

print("\n\033[31mO número {} é divisível por {} números!!\033[m".format(num, cont))

if cont > 0 or cont < 3:
    print("\nO número \033[33m{} é um número primo\033[m.".format(num))
else: 
    print("\n\nO número \033[31m{} não é número primo\033[m.".format(num))