from datetime import date

print('='*50)
print("CLASSIFICANDO ATLETAS")
print('='*50)

nasc = int(input("Digite o ano em que nasceu: "))
ano_atual = date.today().year
idade = ano_atual - nasc

if idade <= 0:
    print("Não existe essa idade.")
elif idade <= 9:
    print("CATEGORIA: MIRIM por ter {} ano(s)".format(idade)) 
elif idade <= 14:
    print("CATEGORIA: INFANTIL por ter {} anos.".format(idade))
elif idade <=19: 
    print("CATEGORIA: JUNIOR por ter {} anos.".format(idade))
elif idade <= 20: 
    print("CATEGORIA: SÊNIOR por ter {} anos.".format(idade))
else:   
    print("CATEGORIA: MASTER por ter {} anos.".format(idade))