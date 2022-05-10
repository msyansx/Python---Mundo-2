from time import sleep 

print("="*50)
print("CALCULANDO IMC")
print("="*50)

peso  = float(input("Digite o seu peso: "))
altura = float (input("Digite a sua altura: "))


print("Um momento...\n")
sleep(2)

while peso <= 0 or altura <= 0:
    print("Valores inválidos para o cálculo")
    peso  = float(input("Digite o seu peso: "))
    altura = float (input("Digite a sua altura: "))
 
imc = float(peso / (altura ** 2))   
print("O seu IMC é: {:.2f}".format(imc))

if imc < 18.5:
    print("Você está abaixo do peso")
elif imc < 25: 
    print("Você está com o peso ideal.")
elif imc < 30: 
    print("Você está com sobrepeso.")
elif imc < 40: 
    print("Você está com obesidade.")
else:
    print("Você está com obesidade MÓRBIDA.")