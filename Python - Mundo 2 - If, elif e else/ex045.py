from random import randint 
from time import sleep

print("-----"*5)
print("PEDRA, PAPEL OU TESOURA")
print("-----"*5)

print("""[0] Pedra
[1] Papel
[2] Tesoura\n""")

itens = ('Pedra', 'Papel', 'Tesoura')
rival = randint(0,2)

player = int(input("Digite qual vai ser sua jogada: "))

while player < 0 or player > 2:
    print("Escolha entre 0 e 2.")
    player = int(input("Digite qual vai ser sua jogada: "))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ")

print("====="*6)
print("O computador jogou {}.".format(itens[rival]))
print("O player jogou {}.".format(itens[player]))
print("====="*6)

if player == 0 and rival == 0 or player == 1 and rival == 1 or player == 2 and rival == 2:
    print("EMPATE")
elif player == 0 and rival == 1 or player == 1 and rival == 2 or player == 2 and rival == 0:
    print("COMPUTADOR VENCEU")
else: 
    print("PLAYER VENCEU")

