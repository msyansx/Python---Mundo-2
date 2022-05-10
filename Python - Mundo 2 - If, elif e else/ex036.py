print("="*50)
print("APROVANDO EMPRÉSTIMO PARA COMPRA DE UMA CASA.")
print("="*50)

cliente = str(input("Qual o seu nome? "))
salario = float(input("Qual é o seu salário? "))


print("*"*50)
print("Olá {}, seja bem-vindo ao Banco DedSec!".format(cliente))
print("*"*50)

opcao = int(input("""Deseja adicionar o valor da casa? 
Digite 1 se quer adicionar o valor da casa e 2 se não precisa: """))

casa = float(input("Digite o valor da casa: R$ "))

if opcao == 1: 
    print("\nO valor da casa é R$ {}\n".format(casa))
  
elif opcao == 2:
    print("Obrigado por utilizar os serviços do Banco DedSec!")
else: 
    print("Opção inválida.")

anos = int(input("Em quantos anos deseja pagar a casa? "))
meses = anos*12
mensalidade = casa / meses

if mensalidade < (salario*30)/100:
    print("O valor das parcelas para pagamento em {} anos é de: R$ {:.2f} ".format(anos, mensalidade))
else:    
    print("Infelizmente o valor da mensalidade excede 30% do salário.")