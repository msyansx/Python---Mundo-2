from time import sleep

print('-=-=-='*7)
print("SOMA DOS PARES")
print('-=-=-='*7)


a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o último valor: "))

while b < a:
    print("O segundo valor deve ser maior que o primeiro, tente novamente.")
    print('-=-=-='*3)
    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o último valor: "))

pares = 0

for c in range(a, b+1):
    if c % 2 == 0:
        pares += c
        
print("A soma dos pares é: {}".format(pares))
