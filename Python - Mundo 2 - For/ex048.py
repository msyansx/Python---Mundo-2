from time import sleep

print('-=-=-='*7)
print("SOMA DE MÚLTIPLO DE TRÊS")
print('-=-=-='*7)

n = int(input("Digite o primeiro número do intervalo: "))
x = int(input("Digite o último número do intervalo: "))


while x < n:
    print("Intervalo não válido, tente novamente:")
    n = int(input("Digite o primeiro número do intervalo: "))
    x = int(input("Digite o último número do intervalo: "))

print("Só um momento...")
sleep(2)
print("\n")

soma = 0
contador = 0
for c in range(n, x + 1, 2):
    if c % 3 == 0:  
        contador = contador + 1
        soma = soma + c
print("No intervalo de {} e {}, existem {} números múltiplos de 3.".format(n, x, contador))
print("A soma dos números múltiplos de 3 é: {}".format(soma))
