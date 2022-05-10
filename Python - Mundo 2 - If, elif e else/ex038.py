print("="*50)
print("VALOR: MAIOR, MENOR OU IGUAL")
print("="*50)

num1 = int(input("Digite o valor A: "))
num2 = int(input("Digite o valor B: "))

if num1 > num2:
    print("O valor A é maior que o valor B, segue: {} │ {}".format(num1, num2))
elif num2 > num1:
    print("O valor B é maior que o valor A, segue: {} │ {}".format(num1, num2))
elif num1 == num2 or num2 == num1:
    print("Os dois valores são iguais: {} │ {}".format(num1, num2))
else: 
    print("Erro desconhecido.")