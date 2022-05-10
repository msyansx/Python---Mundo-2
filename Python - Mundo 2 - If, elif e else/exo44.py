print("="*50)
print("CALCULANDO VALORES DOS PRODUTOS")
print("="*50)

produto = float(input("Digite o valor do produto: R$ "))

while produto <= 0:
    print("Este valor não existe.")
    produto = float(input("Digite o valor das compras: R$ "))
    

opcao = int(input("""\nQual a forma de pagamento?
[1] - À vista no dinheiro/cheque.
[2] - À vista no cartão.
[3]- Parcelar no cartão\n\n"""))

a_vista = produto - (produto * 10 / 100)
cart_avista = produto - (produto * 5 / 100)
parc_cart = produto + (produto * 20 / 100 )

while opcao == 0 or opcao >3:
       print("Opção inválida, por favor escolha algumas das opções abaixo.") 
       opcao = int(input("""\nQual a forma de pagamento?
[1] - À vista no dinheiro/cheque.
[2] - À vista no cartão.
[3]- Parcelar no cartão\n\n"""))
       
if opcao == 1:
   print("\033[34mA opção selecionada foi à vista, o valor será de: R$\033[m {}".format(a_vista)) 
elif opcao == 2:
    print("\033[34mA forma de pagamento selecionada foi à vista no cartão de crédito, o valor será de: R$\033[m {}".format(cart_avista))
elif opcao == 3:
    norm = int(input("\nDigite em quantas parcelas você quer fazer este valor: "))
    if norm > 1 and norm <3:
        print("\n\033[33mSerá parcelado em {} vezes. O valor será de\033[m {}".format(norm, produto))
        print("\033[33mO valor mensal das parcelas será de: R$\033[m {}".format(produto / norm))
    elif norm >= 3:
        print("\n\n\033[33mA forma de pagamento selecionada foi de {} vezes no cartão. O novo valor será de: R$\033[33m {} ".format(norm, parc_cart))
        print("\033[33mO valor mensal das parcelas será de: R$\033[m {}".format(parc_cart / norm))