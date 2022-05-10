from time import sleep 

print("-=-=-="*5)
print("TABUADA")
print("-=-=-="*5)

n = int(input("Digite o valor que deseja ver a tabuada: "))
x = int(input("Digite até quantas vezes deseja multiplicar: "))

while n < 0 or x < 0:
    print("Inválido, tente novamente.")
    print("-=-=-=-="*4)
    n = int(input("Digite o valor que deseja ver a tabuada: "))
    x = int(input("Digite até quantas vezes deseja multiplicar: "))

print('Um momento que vamos fazer este cálculo')
sleep(1)
print('\n')

for i in range(0, x + 1):
    print("{} x {} = {}".format(n, i, n*i))



